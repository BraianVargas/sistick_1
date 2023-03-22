from common.db import *
from werkzeug.security import check_password_hash
import json
from flask import *

from usuarios.model import *

def createUserController(requestedData):
     try:
          admin = False
          if "isadmin" in requestedData:
               admin = True
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
          return f"Error. {e}"
     
def getUsersController():
     data = []
     usersList = db.session.query(Usuario).all()
     for user in usersList:
          data.append(user.toJson())
     return data

def checkLoginController(dataJson):
     print(dataJson["username"])
     user = db.session.query(Usuario).filter_by(username = dataJson["username"])
     print(user)
     
     input()