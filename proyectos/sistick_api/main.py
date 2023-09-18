import unittest
import json
from . import app
from modules.users import User  # Ajusta la importación según la ubicación real de tu modelo User

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Desactiva CSRF en las pruebas
        self.app = app.test_client()
        self.user_data = {
            "name": "Nombre de Prueba",
            "username": "usuario_prueba",
            "password": "contrasena_prueba"
        }

    def test_create_user(self):
        response = self.app.post('/users/create_user', json=self.user_data)
        data = json.loads(response.data.decode('utf-8'))

        # Verifica que la respuesta sea exitosa (código de estado 201)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Usuario creado exitosamente')

        # Verifica que el usuario se haya creado en la base de datos
        created_user = User.query.filter_by(username=self.user_data['username']).first()
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.name, self.user_data['name'])

    def tearDown(self):
        # Elimina los usuarios de prueba después de cada prueba
        created_user = User.query.filter_by(username=self.user_data['username']).first()
        if created_user:
            created_user.delete()  # Suponiendo que tienes un método para eliminar usuarios en tu modelo

if __name__ == '__main__':
    unittest.main()
