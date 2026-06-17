from flask import Flask, session, request, redirect, url_for, render_template_string

app = Flask(__name__)
app.secret_key = "Bibip_contador"

@app.route("/contador", methods=["GET", "POST"])
def contador():
        if request.method == "POST" and request.form.get("zerar"):
                session.pop("contador", None)
                # redirect com query param para mostrar 0 sem incrementar no GET seguinte
                return redirect(url_for("contador", zerado=1))

        if request.args.get("zerado") == "1":
                valor = 0
        else:
                session["contador"] = session.get("contador", 0) + 1
                valor = session["contador"]

        return render_template_string(valor=valor)

if __name__ == "__main__":
        app.run(debug=True)