from flask import flask, import request

app = Flask(__name__)

@app.route('/filme/<genero>')
def filme(genero):
    generos = request.args.get('generos')  
    if genero == 'acao':
        return 'Recomendo assistir "Vingadores: Ultimato"'