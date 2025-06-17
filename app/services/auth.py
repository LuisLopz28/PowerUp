from werkzeug.security import check_password_hash
from app.models.user import users, User

def authenticate(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return User(username)
    return None

def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None