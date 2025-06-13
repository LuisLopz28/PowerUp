from flask import Blueprint, render_template

bp = Blueprint('simulador', __name__, url_prefix='/simulador')

@bp.route('/')
def index():
    return render_template('simulador.html')
