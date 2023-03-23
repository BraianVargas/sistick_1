# Importación de librerias
from flask import *
from sqlalchemy import create_engine
from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy


# Importación de módulos propios
from producto import productoBP
from usuarios import userBP
from data.connection import *


app = Flask(__name__,template_folder='templates')
app.config.from_pyfile("data/config.py")


db = SQLAlchemy(app)

app.register_blueprint(productoBP, url_prefix="/product")
app.register_blueprint(userBP, url_prefix="/user")

@app.route("/")
def index():
    return render_template("base.html", logged = False)

if __name__ == '__main__':
    app.run(debug=True)