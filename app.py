from flask import Flask, render_template
from config import DevelopmentConfig
from routes.simulador import simulador_bp  # Importamos el blueprint

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Registramos el blueprint del simulador
app.register_blueprint(simulador_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
