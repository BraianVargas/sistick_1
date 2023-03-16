from sqlalchemy import *


def getDB():
     engine = create_engine('mysql+mysqlconnector://root@localhost/sistick', connect_args={'connect_timeout': 120})
     return engine