from rest_api import *
from flask_cors import CORS

restapi = Blueprint('api', __name__)
CORS(restapi)
api = Api(
    restapi, api_version='1.0', title="Cloudesign REST API",
    description=""
)


# api.add_resource(ParseStrREST,"/api/parsestr")
api.add_resource(ChangeCSSREST,"/api/change/css")
api.add_resource(ChangeScriptREST,"/api/change/script")
api.add_resource(DBModelInitREST,"/api/dbmodel/init")
api.add_resource(BackendREST,"/api/backend")

