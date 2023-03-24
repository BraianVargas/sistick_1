from werkzeug.security import check_password_hash
from sqlalchemy import *
from flask import *
import jsonify

from extensions import db
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
     usersList = db.session.query(Usuario).all()
     for user in usersList:
          data.append(user.toJson())
     return data

def checkLoginController(dataJson):
     user = db.session.query(Usuario).filter_by(username=dataJson["username"]).first()

     if not user or not check_password_hash(user.password, dataJson["password"]):
          flash('Please check your login details and try again.')
          return redirect(url_for('usuario.routes.login'))
     
     else:
          db.session.add(user)
          return True
     
