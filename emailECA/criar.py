import cartasECA
import textwrap
import sys
from reportlab.lib.pagesizes import letter
from fpdf import FPDF
i = 0
j = 0


def validarLogin(nome, senha):
    global j
    with open("login.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split("-")
            if len(dados) == 2 and dados[0] == nome and dados[1] == senha:
                j += 1
    if j != 0:
        return True
    else:
        return False


def salvar(data, destinatario, mensagem, remetente):
    global i
    carta = open("carta" + str(i)+".txt", "a")
    print(data+destinatario+mensagem+remetente)
    carta.write(data+"\n"+destinatario+"\n"+mensagem+"\n"+remetente)
    i += 1

    txt = f"carta{i-1}.txt"
    arquivo = f"carta{i-1}.pdf"
    Tpdf(txt, arquivo)


def Tpdf(txt, arquivo):

    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = txt.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)
        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(arquivo, "F")
