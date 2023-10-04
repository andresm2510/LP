from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
import secrets
import criar
app = Flask(__name__)
app.secret_key = secrets.token_hex(24)
nome = "nulo"
data_atual = datetime.datetime.now().strftime("%d-%m-%Y")


@app.route("/")
def paginicial():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def mail():
    if request.method == "POST":
        global data_atual
        global nome
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        if criar.validarLogin(nome, senha):
            session["nome"] = nome
            session["senha"] = senha
            return render_template("escrever.html", data_atual=data_atual)
        else:
            flash("Usuario ou senha incorretos!", "error")

            return render_template("login.html")
    else:
        print("nao deu")
        return render_template("login.html")


@app.route("/mail", methods=["POST"])
def escreveCarta():
    global nome
    if request.method == "POST":
        destinatario = request.form.get("destinatario")
        mensagem = request.form.get("mensagem")
        if destinatario == "" or mensagem == "":
            flash("Carta sem destinatario ou mensagem!")

        else:
            global data_atual
            criar.salvar(data_atual, destinatario, mensagem, nome)
            return render_template("sucesso.html")


@app.route("/success", methods=["POST"])
def ultimapag():
    global nome
    global data_atual
    opcao = request.form["botao"]
    if opcao == "sim":
        return render_template("escrever.html", data_atual=data_atual)
    else:
        return render_template("bye.html")


@app.route("/bye", methods=["POST"])
def irdnv():
    cont = request.form["botao"]
    if cont == "Voltar para pagina de login":
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
