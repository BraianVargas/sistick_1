from flask import *
from datetime import date

from extensions import db
from tickets.model import *
from usuarios.model import *



def getAllTicketsController():
     data = []
     ticketList = db.session.query(Ticket).all()
     for ticket in ticketList:
          user = db.session.query(Usuario).filter_by(id=ticket.creator_id).first()
          print(user)
          data.append(ticket)
     return data

def createTicketController(data):
     try:
          creator = db.session.query(Usuario).filter_by(username = session["username"]).first()
          assigned= db.session.query(Usuario).filter_by(username = data["assigned_to"].lower()).first()
          
          print(dict(
               title = data["title"],
               description = data["description"],
               creator_id = creator.id,
               assigned_to = assigned.id,
               state = data["state"].lower(),
               date = str(date.today().strftime("%d-%m-%Y"))
          ))
          
          ticket = Ticket(
               data["title"],
               data["description"],
               creator.id,
               assigned.id,
               data["state"].lower(),
               str(date.today().strftime("%d-%m-%Y"))
          )
          print(ticket)

          print(ticket)
          db.session.add(ticket)
          db.session.commit()
          flash("Ticket cargado correctamente")
          return redirect(url_for("ticket_blueprint.index"))
     except Exception as e:
          flash(f"Error al cargar ticket. {e}")
          return redirect(url_for("ticket_blueprint.newTicket"))
