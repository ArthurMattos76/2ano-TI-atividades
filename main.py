from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    mensagem = ''

    if request.method == 'POST':
        nome = request.form['nome']
        if not nome:
            mensagem = "O campo nome é obrigatório!"
        else:
            mensagem = f"Cadastro realizado com sucesso! Bem-vindo, {nome}"
    
    return render_template('cadastro.html', mensagem=mensagem)
app.debug = True

@app.route("/")
def formulario():
    return render_template("index.html")

@app.route("/validacao", methods=["POST"])
def validacao():

    nome = request.form.get('nome','').strip().title()
    email = request.form.get('email','').strip().lower()
    senha = request.form.get('senha','').strip().title()

    return f"""  
    Nome:{nome}<br>
    Email:{email}<br>
    Senha:{senha}
    """

if __name__ == "__main__":
    app.run(debug=True)