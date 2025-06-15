from flask import Blueprint, render_template, request

simulador_bp = Blueprint('simulador', __name__)

@simulador_bp.route('/simulador', methods=['GET', 'POST'])
def simulador():
    resultado = None
    if request.method == 'POST':
        numero = int(request.form['numero'])
        resultado = numero * 10
    return render_template('simulador.html', resultado=resultado)
