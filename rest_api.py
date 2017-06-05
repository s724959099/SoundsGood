from libs.flask_get import *
from SwaggerWrapper import *
from utli.mb_ruturn import *
from libs.flask_Image import flaskImg
from libs.flask_Upload import flaskUpload

from utli.string_parse import *
from utli.FileReading import *

class ParseStrREST(Resource):
    def post(self):
        mytext=json_get("mytext")
        return "ok"

class ChangeCSSREST(Resource):
    def get(self):
        text=args_get("text")
        type=args_get("type")
        css=ChangeCSS(text,type)
        return {
            "link":css.generate()
        }

class ChangeScriptREST(Resource):
    def get(self):
        text=args_get("text")
        type=args_get("type")
        script=ChangeScript(text,type)
        return {
            "link":script.generate()
        }


class DBModelInitREST(Resource):
    def post(self):
        text=json_get("text")
        strParser = StringModel(text)
        strParser.to_list()
        strParser.getClassName()
        msg = strParser.getColumns()

        modelinit = Model_init(msg)
        return {
            "msg":modelinit.str
        }


class BackendREST(Resource):
    def post(self):
        text = json_get("text")
        bg=BackendGenerate(text)
        return {
            "msg":bg.generate()
        }

