from flask import *
import datetime

from extensions import db
from modules.historical.model import LogHistorica
from modules.usuarios.model import *

def createRegister(action, detail):
     try:
          user = db.session.query(Usuario).filter_by(username = session["username"]).first()
          registro = LogHistorica(user.id, action, detail, datetime.datetime.now())
          db.session.add(registro)
          db.session.commit()
          return
     except Exception as e:
          flash(f"Error al cargar registro log. {e}")
          return redirect(url_for("ticket_blueprint.newTicket"))
