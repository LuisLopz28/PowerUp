from flask_login import UserMixin

# Simulación de base de datos en memoria
users = {
    "admin": {"password": "scrypt:32768:8:1$KKIIPaJigA0uv3Jf$e2cdd8511a657cb8cbf8d288dc58474e8e926cfe2c52ce8fdc2603676395bdedfd7a9c60d931fb14a6f5611b5c120d9d7e8e137d345970feb7571d1405c2f9a2", "id": 1}  # Cambiar por hash real
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

    def get_id(self):
        return self.id