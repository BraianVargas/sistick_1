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