from flask import request, render_template, redirect, url_for, session

from tickets import ticketsBP
from tickets.controller import *



@ticketsBP.route("/index", methods=["GET"])
def index():
     if session.get("username") != None:
          data = getAllTicketsController()
          return render_template("ticket/index.html", data = data, logged=True, admin=session["admin"],pagination="")
     else:
          return redirect(url_for("user_blueprint.login"))


@ticketsBP.route("/newTicket",methods=["GET","POST"])
def newTicket():
     users = db.session.query(Usuario).all()
     if request.method == "GET":
          return render_template("ticket/newTicketForm.html", logged = True, admin=session["admin"], users = users)
     else:
          data = request.form.to_dict()
          createTicketController(data)
          return render_template("ticket/newTicketForm.html", logged = True, admin=session["admin"], users = users)
     
@ticketsBP.route("/edit/<int:ticketId>", methods=["GET","POST"])
def editTicket(ticketId):
     editTicketController(ticketId)
     return redirect(url_for("ticket_blueprint.index"))
     
@ticketsBP.route("/delete/<int:ticketId>", methods=["GET","POST"])
def deleteTicket(ticketId):
     print(ticketId)
     return redirect(url_for("ticket_blueprint.index"))
