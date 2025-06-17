from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.services.auth import authenticate

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Por favor, completa todos los campos.", "warning")
            return render_template("login.html")

        user = authenticate(username, password)
        if user:
            login_user(user)
            return redirect(url_for("main.index"))
        else:
            flash("Usuario o contraseña incorrectos.", "danger")
            return render_template("login.html")

    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada correctamente.", "info")
    return redirect(url_for("auth.login"))
