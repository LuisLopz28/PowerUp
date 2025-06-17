from flask_login import UserMixin

# Simulación de base de datos en memoria
users = {
    "admin": {"password": "123456789", "id": 1}  # Cambiar por hash real
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

    def get_id(self):
        return self.id