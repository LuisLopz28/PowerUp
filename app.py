from flask import Flask, render_template, redirect, url_for, request, session, flash
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Nueva forma de inicializar la base de datos
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

# ... (el resto de las rutas se mantienen igual)