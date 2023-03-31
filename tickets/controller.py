from flask import *
from datetime import date

from extensions import db
from tickets.model import Ticket
from usuarios.model import *

def getAllTicketsController():
     ticketList = db.session.query(Ticket).all()
     
     return ticketList

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

def editTicketController(requestedData, ticketId):
    try:
        # Obtener el ticket a editar
        ticket = db.session.query(Ticket).filter_by(id=ticketId).first()

        # Actualizar los campos del ticket con los datos enviados en el formulario
        ticket.title = requestedData['title']
        ticket.description = requestedData['description']
        ticket.assigned_to = requestedData['assigned_to']
        ticket.state = requestedData['state']

        # Guardar los cambios en la base de datos
        db.session.commit()
        flash(f"Ticket actualizado correctamente. Id: {ticket.id} ")
        return 
    except Exception as e:
        flash(f"Error en actualización de ticket. \n {e}")
        return 

