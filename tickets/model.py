import datetime

from extensions import db

class Ticket(db.Model):
     __tablename__ = 'tickets'

     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String, nullable=False)
     description = db.Column(db.String, nullable=False)
     creator_id = db.Column(db.String, nullable=False)
     assigned_to = db.Column(db.String, nullable=False)
     state = db.Column(db.String, nullable=False)
     date = db.Column(db.String, nullable=False)

     def __init__(self,title,description,creator_id,assigned_to,state,date=datetime.datetime.now()):
          self.title = title
          self.description = description
          self.creator_id = creator_id
          self.assigned_to = assigned_to
          self.state = state
          self.date = date


     def __str__(self):
          return f'Ticket({self.toJson()})'

     def toJson(self):
          d = dict(
               __class__ = self.__tablename__,
               __atributos__ = dict(
                    id = self.id,
                    title = self.title,
                    description = self.description,
                    creator_id = self.creator_id,
                    assigned_to = self.assigned_to,
                    state = self.state,
                    date = self.date
               )
          )
          return d