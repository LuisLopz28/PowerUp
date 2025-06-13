from flask import Flask
from routes import home, powerbi, analisis, simulador, estado, auth

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
