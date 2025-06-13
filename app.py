from flask import Flask
from routes import home, auth  # importa solo los módulos que existen

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura'

# Login obligatorio antes de cualquier ruta (excepto login)
from flask import session, redirect, url_for, request

@app.before_request
def requerir_login():
    rutas_publicas = ['login', 'static']
    if not session.get('usuario') and request.endpoint not in rutas_publicas:
        return redirect(url_for('auth.login'))

# Registra los blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(home.bp)

if __name__ == "__main__":
    app.run()
