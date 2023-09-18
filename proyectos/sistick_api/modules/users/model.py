from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    __tablename__ = 'users'
    def __init__(self, id, name, username, password_hash, created_at, updated_at, active, admin):
        self.id = id
        self.name = name
        self.username = username
        self.password_hash = password_hash
        self.created_at = created_at
        self.updated_at = updated_at
        self.active = active
        self.admin = admin

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'



users=[]
def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None