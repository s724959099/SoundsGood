from libs.String_libs import StringProcess as SP


class Column:
    def __init__(self, line):
        self.Name = ""
        self.primary_key = {
            "Type": False,
            "autoincrement": False
        }
        self.autoincrement = False
        self.nullable = False
        self.Type = "db.Integer"
        self.ForeignKey = {
            "Type": False,
            "Value": None,
        }

        self.Name = SP.startWith(line, "=")

        line = SP.remove_first(line, self.Name)
        line_bracket = SP.inBracket(line)
        lineList = line_bracket.split(",")
        try:
            self.Type = line_bracket.split(",")[0].split(".")[1]
        except:
            self.Type= line_bracket.split(",")[0]

        del lineList[0]
        for index, line in enumerate(lineList):
            check_str = "nullable="
            if check_str in line:
                nullbale = SP.endWith(line, check_str)
                if nullbale == "True":
                    self.nullable = True
                else:
                    self.nullable = False
                del lineList[index]
                break

        for index, line in enumerate(lineList):
            check_str = "primary_key="
            if check_str in line:
                val = SP.endWith(line, check_str)
                if val == "True":
                    self.primary_key["Type"] = True

                del lineList[index]
                break

        for index, line in enumerate(lineList):
            check_str = "autoincrement="
            if check_str in line:
                val = SP.endWith(line, check_str)
                if val == "True":
                    self.primary_key["autoincrement"] = True

                del lineList[index]
                break

        for index, line in enumerate(lineList):
            check_str = "db.ForeignKey"
            if check_str in line:
                value = SP.inBracket(line)
                value = SP.remove(value, '"')
                self.ForeignKey = {
                    "Type": True,
                    "Value": value
                }
                del lineList[index]
                break

        if lineList:
            pass
            # raise Exception()

    def generate_init_arg(self):
        not_generateList = ["CreateDate",
                            "ModifiedDate",
                            "ModifiedBy",
                            "SoftDelete", ]
        if self.Name in not_generateList or self.primary_key["autoincrement"]:
            return ""
        else:
            if self.nullable == True:
                return "{}=None,".format(self.Name)
            else:
                return "{},".format(self.Name)

    def generate_init_text(self):
        not_model_dict = {
            "CreateDate": "self.CreateDate = datetime.datetime.now()",
            "CreateBy": "self.CreateBy = CreateBy",
            "ModifiedDate": "self.ModifiedDate = None",
            "ModifiedBy": "self.ModifiedBy = None",
            "SoftDelete": "self.SoftDelete = False",
        }
        if self.primary_key["autoincrement"]:
            return ""
        if self.Name in not_model_dict:
            return not_model_dict[self.Name]
        else:
            return "self.{}={}".format(self.Name, self.Name)


class StringModel:
    """
    從Model String 解析出Class 以及Column 細節
    """

    def __init__(self, msg):
        self.msg = msg

    def to_list(self):
        self.strIO_readlines = SP.to_lines(self.msg)
        self.list = []
        for line in self.strIO_readlines:
            new_line = SP.clearn_enter(line)
            new_line = SP.clear_space(new_line)
            if new_line != "":
                self.list.append(new_line)
        return self.list

    def getClassName(self):
        startName = "class"
        endName = "(db.Model):"
        for line in self.list:
            if startName in line and endName in line:
                newline = line
                newline = SP.remove(newline, startName)
                newline = SP.remove(newline, endName)
                self.className = newline
        return self.className

    def getColumns(self):
        column_check = "db.Column("
        self.columns = []
        for line in self.list:
            if column_check in line:
                column = Column(line)
                self.columns.append(column)

        return self.columns


class Model_init:
    """
    從取得的欄位解析產生__init__ fn
    default
    self.CreateDate = datetime.datetime.now()
    self.CreateBy = CreateBy
    self.ModifiedDate = None
    self.ModifiedBy = None
    self.SoftDelete = False
    """

    def __init__(self, columns):
        self.columns = self.sort_by_not_null(columns)
        str_init_fn = self.generate_fn_arg()
        str_text = self.generate_fn_text()

        self.str = """
        def __init__(
                self,
                {}
        ):
            {}
        """.format(str_init_fn, str_text)

    def generate_fn_text(self):
        lines = ""

        for c in self.columns:
            newLine = c.generate_init_text()
            if newLine != "":
                lines += """{}
            """.format(newLine)

        return lines

    def generate_fn_arg(self):
        lines = ""
        for index, c in enumerate(self.columns, 1):
            newLine = c.generate_init_arg()
            if newLine != "":
                lines += """{}
                """.format(newLine)

        lines = SP.remove_last(lines, "\n")
        return lines

    def sort_by_not_null(self, columns):
        nullList = []
        not_nullList = []
        for c in columns:
            if c.nullable == True:
                nullList.append(c)
            else:
                not_nullList.append(c)

        not_nullList.extend(nullList)
        total_list = not_nullList
        return total_list


class ChangeCSS:
    def __init__(self, text, type):
        self.text = text
        self.type = type

    def generate(self):
        if self.type == "html":
            if self.text.startswith("https"):
                return """<link rel="stylesheet" href="{}"/>""".format(self.text)
            else:
                new_text = self.text.replace("static", "")
                if new_text[0] == "/":
                    new_text = new_text[1:]

                return """<link rel="stylesheet" href="{{ url_for('static', filename='{}')}}"/>""".format(new_text)
        if self.type == "pug":
            if self.text.startswith("https"):
                return """link(ref="stylesheet" href="{}")""".format(self.text)
            else:
                new_text = self.text.replace("static", "")
                if new_text[0] == "/":
                    new_text = new_text[1:]
                return """link(rel="stylesheet" href="{{ url_for('static', filename='{}')}}")""".format(new_text)


class ChangeScript:
    def __init__(self, text, type):
        self.text = text
        self.type = type

    def generate(self):
        if self.type == "html":
            if self.text.startswith("https"):
                return """<script src="{}"></script>""".format(self.text)
            else:
                new_text = self.text.replace("static", "")
                if new_text[0] == "/":
                    new_text = new_text[1:]

                return """<script src="{{ url_for('static', filename='{}')}}"></script>""".format(new_text)
        if self.type == "pug":
            if self.text.startswith("https"):
                return """script(src="{}")""".format(self.text)
            else:
                new_text = self.text.replace("static", "")
                if new_text[0] == "/":
                    new_text = new_text[1:]
                return """script(src="{{ url_for('static', filename='{}')}}")""".format(new_text)


class BackendGenerate:
    def __init__(self, text):
        self.text = text
    def remove_dash(selaf,text):
        newText=text
        while True:
            try:
                index=newText.index("-")
                newText=''.join(newText.split('-', 1))
                newText= newText[:index]+newText[index].upper()+newText[index+1:]
            except:
                break

        return newText

    def generate(self):
        var_list=SP.in_space(self.text,start="<",end=">",dtype="list")
        new_text=self.text.replace("/","_")
        new_text = SP.remove(new_text,"<")
        new_text = SP.remove(new_text, ">")
        new_text=self.remove_dash(new_text)
        var=", ".join(var_list)
        new_text=new_text[1:]

        result_template = \
"""@app.route("{}")
def {}({}):
    return render_template("{}.html",**locals())
""".format(self.text,new_text,var,new_text)

        return result_template


if __name__ == "__main__":
    MSG = """



class TableColumn(db.Model):
    __tablename__ = 'TableColumn'
    TableColumnId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TableId = db.Column(db.Integer, db.ForeignKey("Table.TableId"), nullable=False)
    Name = db.Column(db.String(256), nullable=False)
    Comment = db.Column(db.String(256), nullable=True)
    SoftDelete = db.Column(TINYINT, nullable=False)
    CreateDate = db.Column(db.DateTime(timezone=True), nullable=False)
    CreateBy = db.Column(db.String(128), nullable=False)
    ModifiedDate = db.Column(db.DateTime(timezone=True), nullable=True)
    ModifiedBy = db.Column(db.String(128), nullable=True)
    Html = db.Column(db.TEXT, nullable=True)
    MarkDown = db.Column(db.TEXT, nullable=True)
"""
    strParser = StringModel(MSG)
    AAA = strParser.to_list()
    AAB = strParser.getClassName()
    AAC = strParser.getColumns()

    modelinit = Model_init(AAC)
    # A = 'OrderId=db.Column(db.Integer,db.ForeignKey("Order.OrderId"),nullable=False)'
    # AB = StringProcess.inBracket(A)
    # AC = StringProcess.inBracket(AB)

    print(modelinit.str)

    print("done")
