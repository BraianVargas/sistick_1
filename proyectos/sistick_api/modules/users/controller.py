from .model import User
from common.db import *

# db, c = getDB()


def create_user(data):
    """
    Crea un nuevo usuario a partir de un JSON con los datos del usuario.
    
    Args:
        data (dict): Un diccionario con los datos del usuario, por ejemplo:
            {
                "name": "Nombre del Usuario",
                "username": "nombredeusuario",
                "password": "contraseña",
                "active": True,  # Opcional, si deseas establecerlo como activo
                "admin": False   # Opcional, si deseas establecerlo como administrador
            }

    Returns:
        User: El objeto de usuario creado y guardado en la base de datos.
    """
    name = data.get("name")
    username = data.get("username")
    password = data.get("password")
    active = data.get("active", True)  # Valor predeterminado es True
    admin = data.get("admin", False)    # Valor predeterminado es False

    # Verifica que no exista un usuario con el mismo nombre de usuario
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return None  # Puedes manejar esto según tus necesidades, por ejemplo, lanzando una excepción o devolviendo un error JSON.

    # Crea un nuevo usuario
    new_user = User(
        name=name,
        username=username,
        password=password,
        active=active,
        admin=admin
    )

    # Agrega el nuevo usuario a la base de datos
    db.session.add(new_user)
    db.session.commit()

    return new_user
