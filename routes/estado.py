from flask import Blueprint, render_template

bp = Blueprint('estado', __name__, url_prefix='/estado')

@bp.route('/')
def index():
    return render_template('estado.html')
