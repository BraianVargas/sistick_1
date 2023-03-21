import flask
from flask import request, render_template, redirect, url_for
import werkzeug

from usuarios import userBP
from usuarios.model import *
from usuarios.controller import *


@userBP.route("/")
@login_required
def index():
     return "Index User"

# Login route. This get the data entry from the login form 
# and validate the user for the access to the app
@userBP.route("/login", methods = ['GET','POST'])
def login():
     if request.method == 'POST':
          # Replace ALl request.form for reques.get_json
          if "username" in session: 
               print(session["username"])
          status = checkLoginController(
               request.form['username'],
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
          data = request.form.to_dict()
          statusMessage = createUserController(data)
          return statusMessage
     else:
          return render_template("user/registerForm.html")

# Ruta para obtener registros de la base de datos.
# Este método tomará los últimos 100 registros.
@userBP.route("/getAll", methods = ['GET','POST'])
def getAllUsers():
     if request.method == 'GET':
          usersList = getUsersController()
          return usersList
     else:
          return "Create User Route"

@userBP.route("/logout", methods = ["GET","POST"])
def logout():
     session.pop("username")
     return redirect(url_for("/user/login"))

# # Ruta para obtener registros de la base de datos.
# # Este método tomará los últimos 100 registros.
# @userBP.route("/getAll", methods = ['GET','POST'])
# def getAllUsers():
#      if request.method == 'GET':
#           usersList = getUsersController()
#           return usersList
#      else:
#           return "Create User Route"
