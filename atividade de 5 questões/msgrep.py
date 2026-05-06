from flask import Flask

app = Flask(__name__)

@app.route('/repetir/<palavras>/<int:vezes>')
def repetir(palavras, vezes):
    return (f"{palavras} " * 3 * vezes).strip()