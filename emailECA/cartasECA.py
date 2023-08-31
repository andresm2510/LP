from flask import Flask, render_template, request
import datetime
import criar
app = Flask(__name__)
nome


@app.route("/")
def paginicial():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def mail():
    if request.method == "POST":
        global nome
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        '''
        criar verificaçao pra fazer o login
        '''
        return render_template("/mail")
    else:
        print("deu errado")

        return ("login.html")


@app.route("/mail", methods=["POST"])
def escreveCarta():
    data_atual = datetime.datetime.now().strftime("%d-%m-%Y")
    return render_template("esccrever.html", data_atual=data_atual)


'''
criar.salvar(data_atual, destinatario, mensagem, nome)]
colocar funçao para pegar a mensagem e o destinatario  e dps usar a linha acima para criar o txt
'''
