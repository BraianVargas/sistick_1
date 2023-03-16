from flask import Blueprint

productoBP = Blueprint('product_blueprint', __name__)

from .routes import *