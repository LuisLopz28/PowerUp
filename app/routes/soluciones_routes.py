from flask import Blueprint, render_template
from flask_login import login_required

soluciones_bp = Blueprint("soluciones", __name__, url_prefix="/soluciones")

@soluciones_bp.route("/limpieza")
@login_required
def limpieza():
    return render_template("soluciones/limpieza.html")