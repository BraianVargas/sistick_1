from flask import *
from flask_sqlalchemy import pagination
import datetime

from extensions import db
from tickets.model import Ticket
from usuarios.model import *

def getAllTicketsController():
     page = db.paginate((db.select(Ticket).order_by(Ticket.id.asc())))
     return page

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
               str((datetime.datetime.now()))
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
          ticket.lastmodif = datetime.datetime.today()
          ticket.state = requestedData['state']
          if (ticket.state.lower() == "cerrado"):
               ticket.sysactive = '0'

          # Guardar los cambios en la base de datos
          db.session.commit()
          flash(f"Ticket actualizado correctamente. Id: {ticket.id} ")
          return 
     except Exception as e:
          flash(f"Error en actualización de ticket. \n {e}")
          return 

