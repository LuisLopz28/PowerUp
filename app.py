from flask import Flask
from routes import home, powerbi, analisis, simulador, estado, auth
from flask import redirect, url_for, session, request

@app.before_request
def require_login():
    rutas_libres = ['auth.login', 'auth.register', 'static']  # si tienes un registro
    if 'user' not in session and request.endpoint not in rutas_libres:
        return redirect(url_for('auth.login'))
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Registrar blueprints (rutas separadas)
app.register_blueprint(home.bp)
app.register_blueprint(powerbi.bp)
app.register_blueprint(analisis.bp)
app.register_blueprint(simulador.bp)
app.register_blueprint(estado.bp)
app.register_blueprint(auth.bp)

if __name__ == "__main__":
    app.run(debug=True)
