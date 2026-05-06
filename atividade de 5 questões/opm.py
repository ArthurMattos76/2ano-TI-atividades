from flask import Flask

app = Flask(__name__)

@app.route('/<n1>/<n2>')
def soma(n1, n2):
    resultado = int(n1) + int(n2)
    return f"A soma de {n1} e {n2} é: {resultado}"