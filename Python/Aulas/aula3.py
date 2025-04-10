# loop / estrutura de repetição

def contagem():
    primeiro = int(input("Digite o primeiro número: "))
    segundo = int(input("Digite o número final: "))
    for numero in range(primeiro,segundo):
        print(numero)

contagem()

def tabuada_10():
    for i in range (1,11):
        for p in range(1,11):
            print(f"{i} x {p} = {i*p}")

tabuada_10()

def media_notas():
    soma = 0
    for i in range(4):
        nota = float(input("Diga a sua nota: "))
        soma += nota
    media = soma/4
    print(media)

media_notas()