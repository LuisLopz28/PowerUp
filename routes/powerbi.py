from flask import Blueprint, render_template

bp = Blueprint('powerbi', __name__, url_prefix='/powerbi')

@bp.route('/')
def index():
    return render_template('powerbi.html')
