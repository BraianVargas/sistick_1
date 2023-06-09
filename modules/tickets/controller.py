from flask import *
import datetime

from extensions import db
from modules.tickets.model import Ticket
from modules.usuarios.model import *
from modules.historical.controller import *


def getAllTicketsController():
     tickets = db.paginate((db.select(Ticket).order_by(Ticket.id.desc()).limit(200)), per_page=10)
     return tickets

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
          createRegister("Create",f"Creación de ticket {ticket.id}")

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
          createRegister("Edit", f"Ticket {ticket.id}. User: {session['username']}")

          flash(f"Ticket actualizado correctamente. Id: {ticket.id} ")
          return 
     except Exception as e:
          flash(f"Error en actualización de ticket. \n {e}")
          return 

