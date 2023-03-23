from werkzeug.security import check_password_hash
from sqlalchemy import *
from flask import *

import app
from data.connection import *
from usuarios.model import *

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
          return redirect(url_for('user_blueprint.login'))
     except Exception as e:
          return f"Error. createUserController. -> \n {e}"
     
def getUsersController():
     data = []
     usersList = app.db.session.query(Usuario).all()
     for user in usersList:
          data.append(user.toJson())
     return data

def checkLoginController(dataJson):
     query = app.db.session.query(Usuario).filter_by(username = dataJson["username"]).all()
     for u in query:
          print(u)
          if check_password_hash(u.password, dataJson["password"]):
               print("LOGGED")
               session.clear()
               db.session.add(u)
               return True
          else:
               error =  "Usuario o contraseña incorrecto"
               return error

     input() 