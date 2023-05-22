from flask import request, render_template, redirect, url_for, session
import werkzeug

from modules.usuarios import userBP
from modules.usuarios.model import Usuario
from modules.usuarios.controller import *
from modules.historical.controller import *


@userBP.route("/")
def index():
     return "Index User"

# Login route. This get the data entry from the login form 
# and validate the user for the access to the app
@userBP.route("/login", methods = ['GET','POST'])
def login():
     if request.method == 'POST':
          status = checkLoginController(request.form.to_dict())
          if status == True:
               createRegister("Login",f"User: {session['username']}")
               return redirect(url_for("ticket_blueprint.assignedToMe"))
          else:
               return render_template("user/LoginForm.html", error=status)
     else:
          if session.get("username") != None:
               return render_template("user/index.html", logged = True)
          else:
               return render_template("user/LoginForm.html")

# Método para crear usuario. Toma la info del JSON recibido,
# genera el modelo y almacena en la base de datos
@userBP.route("/create", methods = ['GET','POST'])
def createUser():
     if "username" in session:
          admin = db.session.query(Usuario).filter_by(username = session["username"]).first()
          if admin.admin == "admin":
               if request.method == 'POST':
                    data = request.form.to_dict()
                    statusMessage = createUserController(data)
                    return statusMessage
               else:
                    return render_template("user/registerForm.html")
          else:
               return redirect(url_for("ticket_blueprint.index"))
     else:
          return redirect(url_for("user_blueprint.login"))


# Ruta para obtener registros de la base de datos.
# Este método tomará los últimos 100 registros.
@userBP.route("/getAll", methods = ['GET','POST'])
def getAllUsers():
     if request.method == 'GET':
          usersList = getUsersController()
          return usersList
     else:
          return "ERROR"

@userBP.route("/logout", methods = ["GET","POST"])
def logout():
     createRegister("Logout",f"User: {session['username']}")
     session.pop("username")
     return redirect(url_for("user_blueprint.login"))

@userBP.route("/user_dashboard", methods = ["GET", "POST"])
def indexUserDashboard():
     users, loginReg = getAllUsersToDashboard()
     return render_template("user/dashboard_user.html", logged=True, username = session["username"], admin = session['admin'], users = users, logs=loginReg)