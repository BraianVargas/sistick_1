from flask import Blueprint

ticketsBP = Blueprint('ticket_blueprint', __name__)

@ticketsBP.before_request
def validate_user_session():
     if "username" not in session:
          return redirect(url_for("user_blueprint.login"))


from .routes import *