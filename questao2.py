from flask import Flask, render_template   

app = Flask(__name__)

@app.route('/operacao/<tipo>/<int:num1>/<int:num2>')
def operacao(tipo, num1, num2):
     if tipo == "soma": 
        resultado = num1 + num2
        return resultado
     elif tipo == "subtracao":
        resultado = num1 - num2
        return resultado
     elif tipo == "multiplicacao":
        resultado = num1 * num2
        return resultado
     elif tipo == "divisao":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero"
        return resultado