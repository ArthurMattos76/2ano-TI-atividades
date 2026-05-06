from flask import Flask

app = Flask(__name__)

@app.route('/produto/<nome>/<preco>')
def produto(nome, preco):
    preco = float(preco)
    return f"O produto {nome} custa R${preco}"

