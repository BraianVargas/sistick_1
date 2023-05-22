import datetime

from extensions import db

class LogHistorica(db.Model):
     __tablename__ = 'log_historial'
     id = db.Column(db.Integer, primary_key = True, nullable = False)
     user_id = db.Column(db.Integer,nullable = False)
     action = db.Column(db.String,nullable = False)
     detail = db.Column(db.String,nullable = False)
     date	 = db.Column(db.String,nullable = False)
     
     def __init__(self, userId, action, detail, date = datetime.datetime.now() ):
          self.user_id = userId
          self.action = action
          self.detail = detail
          self.date = date

     def __str__(self):
          return f'log_historial({self.toJson()})'

     def toJson(self):
          d = dict(
               __class__ = self.__tablename__,
               __atributos__ = dict(
                    id = self.id,
                    user_id = self.user_id,
                    action = self.action,
                    date = self.date
               )
          )
          return d