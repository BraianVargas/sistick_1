from common.db import *
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
     usersList = db.session.query(Usuario).all()
     for user in usersList:
          data = json.dumps(user)
          print(data)
     return usersList