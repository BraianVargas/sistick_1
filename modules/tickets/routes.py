from flask import request, render_template, redirect, url_for, session
import datetime
from sqlalchemy import func, DateTime, Time


from modules.tickets import ticketsBP
from modules.tickets.controller import *



@ticketsBP.route("/index", methods=["GET"])
def index():
     users = db.session.query(Usuario).order_by(Usuario.id.desc()).all()   
     data = getAllTicketsController()

     return render_template(
          "ticket/index.html", 
          data = data,
          admin=session["admin"],
          users = users,
          username = session["username"],
          pagination = data,
          endpoint = "ticket_blueprint.index"
     )

@ticketsBP.route("/newTicket",methods=["GET","POST"])
def newTicket():
     users = db.session.query(Usuario).all()
     if request.method == "GET":
          return render_template("ticket/newTicketForm.html", admin=session["admin"], users = users, username=session["username"])
     else:
          data = request.form.to_dict()
          createTicketController(data)
          return render_template("ticket/newTicketForm.html", admin=session["admin"], users = users,  username=session["username"])

@ticketsBP.route("/edit/<int:ticketId>", methods=["GET","POST"])
def editTicket(ticketId):
     if request.method == "GET":
          users = db.session.query(Usuario).all()
          ticket = db.session.query(Ticket).filter_by(id=ticketId).first()
          return render_template("ticket/edit_ticket.html", ticket=ticket, users =users, username=session["username"])
     else:
          data = request.form.to_dict()
          editTicketController(data, ticketId)
          return redirect(url_for("ticket_blueprint.index"))

@ticketsBP.route("/delete/<int:ticketId>", methods=["GET","POST"])
def deleteTicket(ticketId):
     try:
          ticket = db.session.query(Ticket).filter_by(id=ticketId).first()
          # 'Delete' the ticket from the database
          
          db.session.commit()
          flash(f"Ticket eliminado correctamente. Id: {ticket.id} ")
          return redirect(url_for("ticket_blueprint.index"))
     except Exception as e:
          flash(f"Error en actualización de ticket. \n {e}")
          return
     
@ticketsBP.route("/assigned", methods = ["GET","POST"])
def assignedToMe():
     user = db.session.query(Usuario).filter_by(username=session["username"]).first()
     
     today_date = datetime.datetime.today().date()

     end_of_day = datetime.time(23, 59, 59)
     end_of_day_datetime = datetime.datetime.combine(datetime.datetime.today(), end_of_day)

     filter_condition1 = ((Ticket.state == "cerrado") &
                    (func.date(Ticket.lastmodif) == today_date) &
                    (Ticket.lastmodif.cast(DateTime) <= end_of_day_datetime))
     filter_condition2 = ((Ticket.sysactive == '0') &
                    (func.date(Ticket.lastmodif) == today_date) &
                    (Ticket.lastmodif.cast(DateTime) <= end_of_day_datetime))

     print(str(func.Ticket.lastmodif))

     tickets = db.session.query(Ticket).filter(

          (Ticket.assigned_to == user.id) & 
          (
               (Ticket.state == "abierto") | 
               filter_condition1|
               (Ticket.sysactive == '1') |
               ((Ticket.sysactive == '0') & (((str(Ticket.lastmodif)).split(' '))[0] == datetime.datetime.today().date()))
          )
     ).all()

     users = db.session.query(Usuario).all()
     return render_template("ticket/assigned.html", tickets=tickets, data = tickets, users =users, admin=session["admin"], username=session["username"])