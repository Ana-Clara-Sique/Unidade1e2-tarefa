from flask import render_template , request
from models.problema import Problema

def problema_controller():
    if request.method == 'POST':
        numero_macas_inicial = int(request.form['numero_macas_inicial'])
        numero_macas_dadas = int(request.form['numero_macas_dadas'])
        problema = Problema(numero_macas_inicial, numero_macas_dadas)
        resultado = problema.calcular_macas_restantes()
        return render_template('problema.html',resultado=resultado)
    return render_template('index.html')