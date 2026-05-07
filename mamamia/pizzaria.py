from flask import flask, render_template, request, redirect, url_for
app = flask(__name__)

@app.route('/pizzaria/<sabor>')
def pizzaria(sabor):
    return render_template('pizzaria.html', sabor=sabor)

def sabor(sabor):
    if sabor == 'margherita':
        return render_template('margherita.html')
    elif sabor == 'pepperoni':
        return render_template('pepperoni.html')    

    if __name__ == '__main__':
        app.run(debug=True)