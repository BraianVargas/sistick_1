from flask import *
from datetime import date

from extensions import db
from tickets.model import Ticket
from usuarios.model import *



def getAllTicketsController():
     data = []
     i = 0
     ticketList = db.session.query(Ticket).all()
     for ticket in ticketList:
          creator = db.session.query(Usuario).filter_by(id=ticket.creator_id).first()
          assigned = db.session.query(Usuario).filter_by(id=ticket.assigned_to).first()
          ticket.creator_id = creator.username          
          ticket.assigned_to = assigned.username
          
          data.append(ticket)

     return data

def createTicketController(data):
     try:
          creator = db.session.query(Usuario).filter_by(username = session["username"]).first()
          assigned= db.session.query(Usuario).filter_by(username = data["assigned_to"].lower()).first()
          
          ticket = Ticket(
               data["title"],
               data["description"],
               creator.id,
               assigned.id,
               data["state"].lower(),
               str(date.today().strftime("%d-%m-%Y"))
          )
          db.session.add(ticket)
          db.session.commit()

          flash("Ticket cargado correctamente")
          return redirect(url_for("ticket_blueprint.index"))
     except Exception as e:
          flash(f"Error al cargar ticket. {e}")
          return redirect(url_for("ticket_blueprint.newTicket"))

def editTicketController(ticketId):
     ticket = db.session.query(Ticket).filter_by(id = ticketId).first()
     return ""