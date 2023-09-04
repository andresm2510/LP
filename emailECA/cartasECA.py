from flask import Flask, render_template, request, redirect, session, url_for, flash
import datetime
import secrets
import criar
app = Flask(__name__)
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
        '''
        criar verificaçao pra fazer o login
        '''
        return redirect("escrever.html", data_atual=data_atual)
    else:
        print("deu errado")

        return ("login.html")


@app.route("/mail", methods=["POST"])
def escreveCarta():
    global nome
    if request.method == "POST":
        destinatario = request.form.get("destinatario")
        mensagem = request.form.get("mensagem")
        if destinatario == "" or mensagem == "":
            '''imprimir mensagem de erro'''

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
