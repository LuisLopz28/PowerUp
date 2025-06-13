from flask import Blueprint, render_template, session, redirect, url_for

powerbi_bp = Blueprint('powerbi', __name__, url_prefix='/powerbi')

@powerbi_bp.route('/')
def index():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('powerbi/index.html')

