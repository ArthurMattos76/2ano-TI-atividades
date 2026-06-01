from flask import render_template, request

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

