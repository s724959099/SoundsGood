from utli.string_parse import *


class FileBase:
    startIndex = 0
    endIndex = 0

    @classmethod
    def is_end(cls, line):
        if line == "":
            return True
        else:
            return False


class FileImport(FileBase):
    @classmethod
    def is_start(cls, line):
        if line.startswith("from") and "import" in line:
            return True
        else:
            return False


class FileFlask(FileBase):
    @classmethod
    def is_start(cls, line):
        if line.startswith("app") and "Flask" in line:
            return True
        else:
            return False


class FileClass(FileBase):
    @classmethod
    def is_attr_start(cls, line):
        startName = "class"
        endName = "(db.Model):"
        if startName in line and endName in line:
            return True
        else:
            return False

    @classmethod
    def is_attr_end(cls, line):
        return cls.is_end(line)

    @classmethod
    def is_init_start(cls, line):
        startName = "def"
        endName = "__init__"
        if startName in line and endName in line:
            return True
        else:
            return False

    @classmethod
    def is_init_end(cls,line):
        return cls.is_end(line)



class FileClassAttr(FileBase):
    pass


class FileClassInit(FileBase):
    pass


class FileMain(FileBase):
    @classmethod
    def is_start(cls, line):
        if line.startswith("if") and "__main__" in line:
            return True
        else:
            return False


class baseStatus:
    def __init__(self):
        """
        1: 未啟動
        2: start
        3: end
        """
        self.statusList = [1, 2, 3]
        self.index = 0
        self.status = self.statusList[self.index]

    def turn(self):
        self.index += 1
        if self.index==len(self.statusList):
            self.index=0
        self.status = self.statusList[self.index]


class FileClassStatus(baseStatus):
    def __init__(self):
        """
        1: 未進入ClassAttr
        2: 進入ClassAttr
        3: 離開ClassAttr
        4: 進入ClassInit
        1: 未進入ClassAttr
        """
        super().__init__()
        self.statusList = [1, 2, 3, 4]


def generate_FileImport(process_new_lines):
    fileImportStatus = baseStatus()
    fileImport = FileImport()
    for index, line in enumerate(process_new_lines):
        if fileImportStatus.status != 3:
            if FileImport.is_start(line) and fileImportStatus.status == 1:
                fileImportStatus.turn()
                fileImport.startIndex = index
            if FileImport.is_end(line) and fileImportStatus.status == 2:
                fileImportStatus.turn()
                fileImport.endIndex = index - 1
        else:
            break

    return fileImport


def generate_process_line(new_lines):
    process_new_lines = []
    for index, new_line in enumerate(new_lines):
        newLine = SP.clear_space(new_lines[index])
        process_new_lines.append(SP.clearn_enter(newLine))

    return process_new_lines


def generate_FileFlask(process_new_lines):
    fileFlaskStatus = baseStatus()
    fileFlask = FileFlask()
    for index, line in enumerate(process_new_lines):
        if fileFlaskStatus.status != 3:
            if fileFlask.is_start(line) and fileFlaskStatus.status == 1:
                fileFlaskStatus.turn()
                fileFlask.startIndex = index
            if fileFlask.is_end(line) and fileFlaskStatus.status == 2:
                fileFlaskStatus.turn()
                fileFlask.endIndex = index - 1
        else:
            break

    return fileFlask


def generate_fileClassList(process_new_lines):
    fileclassStatus = FileClassStatus()
    fileClassList = []
    done = True

    for index, line in enumerate(process_new_lines):
        if done:
            fileClass = FileClass()
            done = False
        if fileClass.is_attr_start(line) and fileclassStatus.status == 1:
            fileclassStatus.turn()
            fileClass.attr_startIndex = index

        if fileClass.is_attr_end(line) and fileclassStatus.status == 2:
            fileclassStatus.turn()
            fileClass.arrt_endIndex = index - 1

            if fileClass.is_init_start(process_new_lines[index + 1]) != True and fileclassStatus.status == 3:
                fileclassStatus.status = 1
                done = True

        if fileClass.is_init_start(line) and fileclassStatus.status == 3:
            fileclassStatus.turn()
            fileClass.init_startIndex = index

        if fileClass.is_init_end(line) and fileclassStatus.status == 4:
            fileclassStatus.turn()
            fileClass.init_endIndex = index - 1
            done = True

        if done:
            fileClassList.append(fileClass)

    return fileClassList


def generate_FileMain(process_new_lines):
    fileMainStatus = baseStatus()
    fileMain = FileMain()
    for index, line in enumerate(process_new_lines):
        if fileMainStatus.status != 3:
            if fileMain.is_start(line) and fileMainStatus.status == 1:
                fileMainStatus.turn()
                fileMain.startIndex = index
            if fileMain.is_end(line) and fileMainStatus.status == 2:
                fileMainStatus.turn()
                fileMain.endIndex = index - 1
        else:
            break

    return fileMain


if __name__ == "__main__":
    with open("dbModel.py", "r+") as f:
        lines = f.readlines()
        process_new_lines = generate_process_line(lines)

        fileImport = generate_FileImport(process_new_lines)
        fileFlask = generate_FileFlask(process_new_lines)
        fileClassList = generate_fileClassList(process_new_lines)
        fileMain = generate_FileMain(process_new_lines)

    print("done")
