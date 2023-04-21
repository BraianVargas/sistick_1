from werkzeug.security import check_password_hash
from sqlalchemy import *
from flask import *

from extensions import db
from modules.usuarios.model import *
from modules.historical.controller import *

def createUserController(requestedData):
     try:
          admin = "usuario"
          if "isadmin" in requestedData:
               admin = "admin"
          user = Usuario(
               requestedData['username'],
               requestedData['email'],
               requestedData['password'],
               admin
          )
          db.session.add(user)
          db.session.commit()
          createRegister("Create", f"Create User Profile. User: {user.username}")

          # ---- MODIFICAR: enviar al dashboard
          return redirect(url_for('user_blueprint.login'))
          # ---- !!!!!!!!!!!!!
     except Exception as e:
          return f"Error. createUserController. -> \n {e}"
     
def getUsersController():
     data = []
     usersList = db.session.query(Usuario).all()
     for user in usersList:
          data.append(user.toJson())
     createRegister("Consult", f"Consult to profile. User: {user.username}")
     return data

def checkLoginController(dataJson):
     user = db.session.query(Usuario).filter_by(username=dataJson["username"]).first()

     if not user or not check_password_hash(user.password, dataJson["password"]):
          flash('Usuario o contraseña incorrectos. Reintente.')
          return redirect(url_for("user_blueprint.login"))
     else:
          session["username"]=user.username
          session["admin"]=user.admin
          return True
     
