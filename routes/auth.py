from flask import Blueprint, render_template, request, redirect, session, url_for, flash
import sqlite3

bp = Blueprint('auth', __name__, url_prefix='/auth')

def validar_usuario(username, password):
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validar_usuario(username, password):
            session['user'] = username
            return redirect(url_for('home.index'))
        else:
            flash('Credenciales inválidas', 'error')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))
