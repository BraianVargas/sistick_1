from flask import Flask
from flask_login import LoginManager

from modules.users.model import *


app = Flask(__name__)
app.config.from_pyfile('data/config.py')

login_manager = LoginManager(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


# ----------------------------- IMPORTA Y REGISTRA LOS BLUEPRINTS --------------------------------------
from modules.users import usersBP
app.register_blueprint(usersBP, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
