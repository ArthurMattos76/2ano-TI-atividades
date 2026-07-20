from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO = "livros.json"


def carregar_livros():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_livros(livros):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(livros, f, indent=4, ensure_ascii=False)


@app.route("/", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        titulo = request.form["titulo"].strip()
        autor = request.form["autor"].strip()
        ano = request.form["ano"].strip()
        categoria = request.form["categoria"].strip()
        quantidade = request.form["quantidade"].strip()

        if not all([titulo, autor, ano, categoria, quantidade]):
            return render_template("cadastro.html", erro="Preencha todos os campos.")

        if not ano.isdigit():
            return render_template("cadastro.html", erro="Ano deve conter apenas números.")

        if not quantidade.isdigit() or int(quantidade) <= 0:
            return render_template("cadastro.html", erro="Quantidade deve ser maior que zero.")

        livros = carregar_livros()

        livros.append({
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "categoria": categoria,
            "quantidade": int(quantidade)
        })

        salvar_livros(livros)

        return redirect(url_for("livros"))

    return render_template("cadastro.html")


@app.route("/livros")
def livros():
    lista = carregar_livros()
    return render_template("livros.html", livros=lista)


@app.route("/buscar", methods=["GET", "POST"])
def buscar():

    resultado = None
    mensagem = None

    if request.method == "POST":

        titulo = request.form["titulo"].strip().lower()

        livros = carregar_livros()

        for livro in livros:
            if livro["titulo"].strp().lower() == titulo:
                resultado = livro
                break

        if resultado is None:
            mensagem = "Livro não encontrado."

    return render_template("buscar.html",
                           resultado=resultado,
                           mensagem=mensagem)


@app.route("/editar/<int:indice>", methods=["GET", "POST"])
def editar(indice):

    livros = carregar_livros()

    if request.method == "POST":

        titulo = request.form["titulo"].strip()
        autor = request.form["autor"].strip()
        ano = request.form["ano"].strip()
        categoria = request.form["categoria"].strip()
        quantidade = request.form["quantidade"].strip()

        if not all([titulo, autor, ano, categoria, quantidade]):
            return "Todos os campos são obrigatórios."

        if not ano.isdigit():
            return "Ano inválido."

        if not quantidade.isdigit() or int(quantidade) <= 0:
            return "Quantidade inválida."

        livros[indice] = {
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "categoria": categoria,
            "quantidade": int(quantidade)
        }

        salvar_livros(livros)

        return redirect(url_for("livros"))

    return render_template("editar.html",
                           livro=livros[indice],
                           indice=indice)


@app.route("/excluir/<int:indice>")
def excluir(indice):

    livros = carregar_livros()

    livros.pop(indice)

    salvar_livros(livros)

    return redirect(url_for("livros"))


if __name__ == "__main__":
    app.run(debug=True)