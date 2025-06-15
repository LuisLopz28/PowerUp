from flask import Flask, render_template, request, redirect, url_for
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/simulador', methods=['GET', 'POST'])
def simulador():
    resultado = None
    if request.method == 'POST':
        numero = int(request.form['numero'])
        resultado = numero * 10  # simulación simple
    return render_template('simulador.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
