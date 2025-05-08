import os

def pasta():
    nome = input("Digite o nome da nova pasta: ")
    os.mkdir(nome)
    diretorio_atual = os.getcwd()
    diretorios = os.listdir(diretorio_atual)
    print(diretorios)
pasta()