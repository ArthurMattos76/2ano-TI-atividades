from flask import Flask, render_template_string, redirect, url_for, request, session, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = "change_this_secret"

USER = {
    "username": "usuario",
    "password": "senha",
    "name": "Lucas",
    "favorite_color": "Azul",
    "favorite_language": "Python",
    "motto": "Aprendendo sempre e nunca desistindo."
}

@app.route("/")
def index():
    if session.get("logged_in"):
        return redirect(url_for("secret"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        if request.form.get("username") == USER["username"] and request.form.get("password") == USER["password"]:
            session["logged_in"] = True
            session["name"] = USER["name"]
            return redirect(url_for("secret"))
        message = "Login inválido. Tente novamente."
    # Resposta simples sem HTML
    msgs = get_flashed_messages()
    resp = "Login\n"
    if message:
        resp += f"Erro: {message}\n"
    for m in msgs:
        resp += f"Aviso: {m}\n"
    resp += "Envie usuário e senha via POST para autenticar."
    return resp

@app.route("/secret")
def secret():
    if not session.get("logged_in"):
        flash("Você precisa estar logado para acessar o cantinho secreto.")
        return redirect(url_for("login"))
    name = session.get("name")
    return (
        f"Cantinho Secreto - Olá, {name}!\n"
        f"Cor favorita: {USER['favorite_color']}\n"
        f"Linguagem favorita: {USER['favorite_language']}\n"
        f"Motto: {USER['motto']}\n"
        f"Volte ao painel via /panel"
    )

@app.route("/panel")
def panel():
    if not session.get("logged_in"):
        flash("Você precisa estar logado para acessar o painel.")
        return redirect(url_for("login"))
    # Resposta simples sem HTML
    name = session.get("name")
    return (
        f"Painel\nBem-vindo, {name}.\n"
        f"Acesse o cantinho secreto: /secret\n"
        f"Para sair: /logout\n"
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
 