from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from data.connection import *

# GENERA LA SESION PARA LA BASE DE DATOS
Session = sessionmaker(bind=getDB())
session = Session()


Base = declarative_base()