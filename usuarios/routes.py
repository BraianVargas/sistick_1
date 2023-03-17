import flask
from flask import request, render_template, redirect, url_for
import werkzeug

from usuarios import userBP
from usuarios.model import *
from usuarios.controller import *


@userBP.route("/")
def index():
     return "Index User"

# Login route. This get the data entry from the login form 
# and validate the user for the access to the app
@userBP.route("/login", methods = ['GET','POST'])
def login():
     if request.method == 'POST':
          # Replace ALl request.form for reques.get_json
          status = checkLoginController(
               request.form['username'],
               request.form['password']
          )
          if status:
               return redirect("/user/")
          else:
               return redirect("/user/login")

     else:
          return render_template("user/LoginForm.html")
     
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
          return usersList
     else:
          return "Create User Route"

# # Ruta para obtener registros de la base de datos.
# # Este método tomará los últimos 100 registros.
# @userBP.route("/getAll", methods = ['GET','POST'])
# def getAllUsers():
#      if request.method == 'GET':
#           usersList = getUsersController()
#           return usersList
#      else:
#           return "Create User Route"

