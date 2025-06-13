from flask import Flask, render_template, redirect, url_for, request, session
import sqlite3
from functools import wraps

app = Flask(__name__)
app.secret_key = 'clave_secreta'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'usuario' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

def validar_usuario(usuario, contraseña):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contraseña=?", (usuario, contraseña))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if validar_usuario(usuario, contraseña):
            session['usuario'] = usuario
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Credenciales inválidas')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def home():
    return render_template('home.html')
