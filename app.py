# Importación de librerias
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Importación de módulos propios
from producto import productoBP
from usuarios import userBP
from data.connection import *
import common.db


app = Flask(__name__,template_folder='templates')

db = getDB() # Engine de Base de datos

app.register_blueprint(productoBP, url_prefix="/product")
app.register_blueprint(userBP, url_prefix="/user")

if __name__ == '__main__':
    app.run(debug=True)