import flask
from flask import request
import werkzeug

from usuarios import userBP
from usuarios.model import *
from usuarios.controller import *

@userBP.route("/")
def index():
    return "Index User"


# Método para crear usuario. Toma la info del JSON recibido,
# genera el modelo y almacena en la base de datos
@userBP.route("/create", methods = ['GET','POST'])
def createUser():
     if request.method == 'POST':
          data = request.get_json()
          statusMessage = createUserController(data)
          return statusMessage
     else:
          return "Create User Route"
     
# Ruta para obtener registros de la base de datos.
# Este método tomará los últimos 100 registros.
@userBP.route("/getAll", methods = ['GET','POST'])
def getAllUsers():
     if request.method == 'GET':
          usersList = getUsersController()
          
     else:
          return "Create User Route"

