# Importación de librerias
from flask import *
from flask_sqlalchemy import SQLAlchemy

# Importación de módulos propios
from extensions import db
from modules.usuarios import userBP
from modules.tickets import ticketsBP

app = Flask(__name__,template_folder='templates')
app.config.from_pyfile("data/config.py")

db.init_app(app)

app.register_blueprint(userBP, url_prefix="/user")
app.register_blueprint(ticketsBP, url_prefix="/tickets")

@app.route("/")
def index():
    if "username" in session:
        return render_template("base.html", logged = True, username=session["username"], admin=session["admin"])
    else:
        return render_template("base.html", logged = False)

if __name__ == '__main__':
    app.run(debug=True)