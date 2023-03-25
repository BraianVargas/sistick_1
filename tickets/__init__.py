from flask import Blueprint

ticketsBP = Blueprint('ticket_blueprint', __name__)

from .routes import *