def check_login(username, password):
    # Autenticación básica (puedes conectar a SQLite si quieres algo más robusto)
    users = {
        "luis": "1234",
        "admin": "adminpass"
    }
    return users.get(username) == password