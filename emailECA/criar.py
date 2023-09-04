import cartasECA
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
i = 0


def salvar(data, destinatario, mensagem, remetente):
    global i
    carta = open("carta" + str(i)+".txt", "a")
    print(data+destinatario+mensagem+remetente)
    carta.write(data+"\n"+destinatario+"\n"+mensagem+"\n"+remetente)
    global i
    i += 1
    teste = carta
    pdf(carta, teste)


'''
criar funçcao para mudar esse txt para pdf



def pdf(arquivotxt, arquivo):

    c = canvas.Canvas(arquivo, pagesize=letter)
    with open(arquivotxt, "r") as txt_file:
        lines = txt_file.readlines()

    c.setFont("Helvetica", 12)
    for line in lines:
        c.drawString(100, 700, line)
        c.showPage()
        c.save()
'''
