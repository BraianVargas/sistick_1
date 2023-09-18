from flask import Blueprint

usersBP = Blueprint('user_bp', __name__)

from . import routes