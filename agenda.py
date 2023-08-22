# agenda

i = 0
contatos = {}
saida = True

#editar
def adicionar():

    name = input("Nome: ")
    global contatos
    global i

    if name in contatos:
        print("     O contato ja existe!       \n")

    else:
        tel = input("Telefone: ")
        contatos[name] = tel
        i += 1

    print(contatos)
    print("\n")


def remover():

    global i
    name = input("Qual contato deseja remover?: ")
    if name in contatos:
        del contatos[name]
        i -= 1

    else:
        print("Contato nao encontrado")

    print(contatos)
    print("\n")


def editar():

    name = input("Qual contato deseja editar?: ")
    if name in contatos:
        aux = int(
            input("Deseja alterar o nome ou o numero?\n(1 para nome 2 para numero): "))
        if (aux == 1):
            nameaux = input("Qual nome deseja colocar?: ")
            tel = contatos[name]
            contatos.pop(name)
            contatos[nameaux] = tel

        elif (aux == 2):
            telaux = input("Qual o novo numero de " + name + "?: ")
            contatos[name] = telaux

    else:
        print("Contato nao existe!!")

    print(contatos)


def mostrar():
    name = input("Qual contato deseja encontrar?")
    if name in contatos:
        print("O numero de " + name + " é: " + contatos[name])

    else:
        a = input("Contato nao salvo!! \n Deseja salva-lo?(sim ou nao)")
        if a == "sim":
            adicionar()

        else:
            pass


def sair():
    global saida
    saida = False
    print(contatos)
    print("\n")
    print("       Ateh logo!!!!!!!            \n\n\n")
    return saida


while (saida):
    a = input("O que deseja fazer?\n a para adicionar;\n r para remover;\n e para editar;\n m para mostrar um contato;\n s para sair. ")
    if (a == "a"):
        adicionar()

    elif (a == "r"):
        remover()

    elif (a == "e"):
        editar()

    elif (a == "m"):
        mostrar()

    elif (a == "s"):
        sair()

    else:
        print("Comando invalido!!!!\n Tente novamente! \n")
