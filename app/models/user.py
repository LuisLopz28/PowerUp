from flask_login import UserMixin

# Simulación de base de datos en memoria
users = {
    "admin": {"password": "pbkdf2:sha256:1000000$RIx2qllYCbrg21aM$a37273354dcc85f9270bb1dbd89abdd8c17a6d39ba05c340cd8b8bc67a73c51d", "id": 1}  # Cambiar por hash real
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

    def get_id(self):
        return self.id