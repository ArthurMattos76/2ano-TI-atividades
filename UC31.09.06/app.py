from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def inicio():
    nome = request.cookies.get('nome')
    tema = request.cookies.get('tema', 'claro')

    return render_template('index.html', nome=nome, tema=tema)

@app.route("/salvar_nomes", methods=["POST"])
def salvar_nomes():
    nome = request.form.get('nome')
    tema = request.form.get('tema')

    resp = make_response(redirect(url_for('inicio')))
    resp.set_cookie('nome', nome, max_age=60*60*24*30)  

    return resp

@app.route("/trocar_tema")
def trocar_tema():
    tema_atual = request.cookies.get('tema', 'claro')
    novo_tema = 'escuro' if tema_atual == 'claro' else 'claro'

    resp = make_response(redirect(url_for('inicio')))
    resp.set_cookie('tema', novo_tema, max_age=60*60*24*30)  

    return resp

if __name__ == '__main__':
    app.run(debug=True)