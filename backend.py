from api_urls import api
from rest_api import *

app = Flask(__name__)
app.secret_key = 'edjw8vlsuig2d5djh'
app.register_blueprint(api.blueprint)
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route('/')
def login():
    Title="tset"
    return render_template("index.html",**locals())


@app.route("/change/css")
def change_css():
    return render_template("change_css.html",**locals())

@app.route("/dbmodel/init")
def dbmodel_init():
    return render_template("dbmodel_init.html",**locals())


@app.route("/change/script")
def change_script():
    return render_template("change_script.html",**locals())

@app.route("/backend")
def backend():
    return render_template("backend.html",**locals())

if __name__ == '__main__':
    app.run(debug=True,port=4000)