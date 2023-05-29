from flask import Blueprint

userBP = Blueprint('user_blueprint', __name__)
     
from .routes import *