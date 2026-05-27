from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def recebedados():
    nome = request.form['nome']
    email = request.form['email']   

    return "{} e {}".format(nome, email)

if __name__ == '__main__':
    app.run(debug=True)