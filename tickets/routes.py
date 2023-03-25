from flask import request, render_template, redirect, url_for, session

from tickets import ticketsBP
from tickets.model import Ticket
from tickets.controller import *



@ticketsBP.route("/index", methods=["GET"])
def index():
     if session.get("username") != None:
          data = getAllTicketsController()
          return render_template("ticket/index.html", data = data, logged=True, admin=session["admin"])
     else:
          return redirect(url_for("user_blueprint.login"))