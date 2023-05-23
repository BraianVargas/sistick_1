from flask import Blueprint

userBP = Blueprint('user_blueprint', __name__)

@userBP.before_request
def validate_user_session():
     if "username" not in session:
          return redirect(url_for("user_blueprint.login"))
     
from .routes import *