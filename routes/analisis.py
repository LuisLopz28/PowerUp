from flask import Blueprint, render_template

bp = Blueprint('analisis', __name__, url_prefix='/analisis')

@bp.route('/')
def index():
    return render_template('analisis.html')
