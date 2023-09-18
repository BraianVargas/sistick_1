from flask import * 
from flask_login import login_required, current_user, login_user, logout_user

from modules.users.controller import *
from . import usersBP
from modules.users.model import *
from common.db import getDB



# Login
@usersBP.route('/login', methods=['GET', 'POST'])
def login():
    userData = request.get_json()
    user = User.query.filter_by(username=userData['username']).first()  
    if user is not None and user.check_password(userData['password']):
        login_user(user)
        return jsonify({'message': 'Inicio de sesión exitoso'})
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401


# Logout
@usersBP.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Cierre de sesión exitoso'})


# Ruta para crear un usuario
@usersBP.route('/create_user', methods=['POST'])
def create_new_user():
    data = request.get_json()  # Obtén los datos del usuario desde el JSON del cuerpo de la solicitud

    if not data:
        return jsonify({'message': 'Datos del usuario faltantes o inválidos'}), 400

    new_user = create_user(data)  # Llama al método create_user para crear el usuario

    if new_user:
        return jsonify({'message': 'Usuario creado exitosamente', 'user_id': new_user.id}), 201
    else:
        return jsonify({'message': 'El nombre de usuario ya existe'}), 409


# Asumiendo que hay una vista protegida
@usersBP.route('/protected')
@login_required
def protected():
    return jsonify({'message': 'Contenido protegido'})