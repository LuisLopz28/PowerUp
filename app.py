from flask import Flask, render_template, redirect, url_for, request, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Decorador para login
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'usuario' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form('usuario')
        contraseña = request.form('contraseña')
        # Validación ficticia
        if usuario == 'admin' and contraseña == '1234':
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
