from flask import request, render_template, redirect, url_for, session
import datetime

from tickets import ticketsBP
from tickets.controller import *



@ticketsBP.route("/index", methods=["GET"])
def index():
     if session.get("username") != None:
          data = getAllTicketsController()
          users = db.session.query(Usuario).order_by(Usuario.id.desc()).all()
          return render_template("ticket/index.html", data = data, logged=True, admin=session["admin"], users = users, username = session["username"])
     else:
          return redirect(url_for("user_blueprint.login"))


@ticketsBP.route("/newTicket",methods=["GET","POST"])
def newTicket():
     if session.get("username") != None:
          users = db.session.query(Usuario).all()
          if request.method == "GET":
               return render_template("ticket/newTicketForm.html", logged = True, admin=session["admin"], users = users)
          else:
               data = request.form.to_dict()
               createTicketController(data)
               return render_template("ticket/newTicketForm.html", logged = True, admin=session["admin"], users = users)
     else:
          return redirect(url_for("user_blueprint.login"))

@ticketsBP.route("/edit/<int:ticketId>", methods=["GET","POST"])
def editTicket(ticketId):
     if session.get("username") != None:
          if request.method == "GET":
               users = db.session.query(Usuario).all()
               ticket = db.session.query(Ticket).filter_by(id=ticketId).first()
               return render_template("ticket/edit_ticket.html", logged = True, ticket=ticket, users =users)
          else:
               data = request.form.to_dict()
               editTicketController(data, ticketId)
               return redirect(url_for("ticket_blueprint.index"))
     else:
          return redirect(url_for("user_blueprint.login"))

@ticketsBP.route("/delete/<int:ticketId>", methods=["GET","POST"])
def deleteTicket(ticketId):
     if session.get("username") != None:
          try:
               ticket = db.session.query(Ticket).filter_by(id=ticketId).first()
               # Delete the ticket from the database
               db.session.delete(ticket)
               db.session.commit()
               flash(f"Ticket eliminado correctamente. Id: {ticket.id} ")
               return redirect(url_for("ticket_blueprint.index"))
          except Exception as e:
               flash(f"Error en actualización de ticket. \n {e}")
               return
     else:                                                                                                                                                  
          return redirect(url_for("user_blueprint.login"))
     
@ticketsBP.route("/assigned", methods = ["GET","POST"])
def assignedToMe():
     user = db.session.query(Usuario).filter_by(username=session["username"]).first()
    
     tickets = db.session.query(Ticket).filter(
          (Ticket.assigned_to == user.id) & 
          ((Ticket.state == "abierto") | ((Ticket.state == "cerrado") & (Ticket.date == datetime.datetime.today().date())))
     ).all()

     users = db.session.query(Usuario).all()
     return render_template("ticket/assigned.html", logged = True, tickets=tickets, data = tickets, users =users)