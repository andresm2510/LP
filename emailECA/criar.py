import cartasECA
i = 0
carta = open("carta"+[i]+".txt", "a")


def salvar(data, destinatario, mensagem, remetente):
    global carta
    print(data+destinatario+mensagem+remetente)
    carta[i].write(data+"\n"+destinatario+"\n"+mensagem+"\n"+remetente)
    global i
    i += 1

'''
criar funçcao para mudar esse txt para pdf
'''