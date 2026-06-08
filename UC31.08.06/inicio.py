from flask import (
    Flask, 
    render_template, 
    request, 
    redirect,
    url_for, 
    make_response
)
app = Flask(__name__)

@app.route('/')
def inicio():
    

    tema = request.cookies.get('tema', 'claro')
    return render_template('inicio.html', tema=tema)

@app.route('/tema/<escolhido>')
def trocar_tema(escolhido):
    if escolhido not in ['claro', 'escuro']:
        return redirect(url_for('inicio'))

    resp = make_response(redirect(url_for('inicio')))
    resp.set_cookie('tema', escolhido, max_age=60*60*24*30)  
    return resp

if __name__ == '__main__':
    app.run(debug=True)