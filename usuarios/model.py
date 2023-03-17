import common.db as db

from sqlalchemy import *
from werkzeug.security import generate_password_hash



class Usuario(db.Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __init__(self, username, email, password, type):
        self.username = username
        self.email = email
        self.password = generate_password_hash(
            password,
            method='sha256', salt_length=8
        )
        self.type = type

    def __str__(self):
        return f'Usuario({self.id}, {self.username}, {self.email}, {self.type})'

    def toJson(self):
        d = dict(
            __class__ = self.__tablename__,
            __atributos__ = dict(
                id = self.id,
                username = self.username,
                email = self.email,
                type = self.type
            )
        )
        return d