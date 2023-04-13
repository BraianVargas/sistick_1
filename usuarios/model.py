from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask import session
from extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.String, nullable=False)
    sysactive = db.Column(db.String, nullable=False)


    def __init__(self, username, email, password, admin="usuario"):
        self.username = username
        self.email = email
        self.password = generate_password_hash(
            password,
            method='sha256',
            salt_length=8
        )
        self.admin = admin

    def __str__(self):
        return f'Usuario({self.id}, {self.username}, {self.email}, {self.admin})'

    def toJson(self):
        d = dict(
            __class__ = self.__tablename__,
            __atributos__ = dict(
                id = self.id,
                username = self.username,
                email = self.email,
                admin = self.admin
            )
        )
        return d