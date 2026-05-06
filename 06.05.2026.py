from flask import Flask, render_template

app = Flask(__name__)

@app.route('/arearestrita/<int:id>')
def area_restrita(id):
    if id == 1:
        status = "Cadeado Fechado"
        codigo = """if id == 1:
    status = "Cadeado Fechado" """
    elif id == 2:
        status = "Cadeado Aberto"
        codigo = "elif id == 2:\n    status = \"Cadeado Aberto\""
    else:
        status = "ID inválido. Use 1 ou 2."
        codigo = f"else:\n    status = \"{status}\""
    return render_template("area.html", status=status, codigo=codigo)

if __name__ == "__main__":
    app.run(debug=True)
