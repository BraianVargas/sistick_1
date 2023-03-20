from common.db import *
from werkzeug.security import check_password_hash
from usuarios.model import *
import json


def createUserController(requestedData):
     try:
          user = Usuario(
               requestedData['username'],
               requestedData['email'],
               requestedData['password'],
               requestedData['type'] 
          )
          db.session.add(user)
          db.session.commit()
          return "Registro cargado correctamente"
     except Exception as e:
          return f"Error. {e}"
     
def getUsersController():
     data = []
     usersList = db.session.query(Usuario).all()
     for user in usersList:
          data.append(user.toJson())
     return data

def checkLoginController(user, username,password):
     if db.session.query(Usuario).filter_by(username = user) and db.session.query(Usuario).filter_by(username = password):
          return True
     else:
          return False


