import os

def pasta():
    nome = input("Digite o nome da nova pasta: ")
    os.mkdir(nome)
    diretorios = os.listdir("C:\Users\Senac\Desktop\Mattheus (Não apague)\Python\Atividades")
    arquivos = ""