from flask import Flask, render_template, redirect, url_for, request, session
from functools import wraps
from auth.login import check_login

app = Flask(__name__)
app.secret_key = "supersecretkey"

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if check_login(request.form["username"], request.form["password"]):
            session["logged_in"] = True
            session["user"] = request.form["username"]
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Usuario o contraseña inválidos")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/home")
@login_required
def home():
    return render_template("home.html")

@app.route("/simuladores")
@login_required
def simuladores():
    return render_template("simuladores.html")

@app.route("/simuladores/explotacion")
@login_required
def explotacion():
    return render_template("explotacion.html")

@app.route("/tableros")
@login_required
def tableros():
    return render_template("tableros.html")

@app.route("/contacto")
@login_required
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)
