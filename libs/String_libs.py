import io


class StringProcess:
    @classmethod
    def to_lines(cls, msg):
        strIO = io.StringIO(msg)
        return strIO.readlines()

    @classmethod
    def clearn_enter(cls, line):
        return "".join(line.split("\n"))

    @classmethod
    def clear_space(cls, line):
        return StringProcess.remove(line," ")

    @classmethod
    def remove(self, line, str):
        return line.replace(str, "")

    @classmethod
    def remove_first(self, line, str):
        return line.replace(str, "",1)

    @classmethod
    def remove_last(cls,line,str):
        return ''.join(line.rsplit(str, 1))

    @classmethod
    def startWith(cls, line, str):
        return line.split(str)[0]

    @classmethod
    def endWith(cls, line, str):
        return line.split(str)[1]




    @classmethod
    def in_space(cls,line,start,end,dtype="one"):
        if dtype=="one":
            start_id = 0
            end_id = 0
            for index, char in enumerate(line):
                if char == start:
                    start_id = index
                    break

            for index, char in enumerate(line[::-1]):
                if char == end:
                    end_id = len(line) - index
                    break

            return line[start_id + 1:end_id - 1]
        if dtype=="list":
            datas=[]
            check_type="start"
            start_id = 0
            end_id = 0
            for index, char in enumerate(line):
                if char == start and check_type=="start":
                    start_id = index
                    check_type="end"
                if char == end and check_type=="end":
                    end_id = index
                    check_type="done"

                if check_type=="done":
                    datas.append(line[start_id+1:end_id])
                    check_type = "start"
            return datas



    @classmethod
    def inBracket(cls, line):
        return cls.in_space(line,start="(",end=")")

