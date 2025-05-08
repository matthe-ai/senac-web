print("Descubra agora se você tem acesso à festa.")
def MaiorIdade():
    idade = float(input("Digite a sua idade: "))
    if idade < 18:
        print("Acesso negado")
    else:
        print("Acesso permitido")

MaiorIdade()