import statistics

def lista_media():
    qntd = int(input("Digite quantos números você quer calcular: "))
    numeros = []
    for i in range(qntd):
        n = int(input(f"Digite o {i+1}° número: "))
        numeros.append(n)
    media = statistics.mean(numeros)
    mediana = statistics.median(numeros)
    moda = statistics.mode(numeros)
    print(f"A media dos números {numeros} é: {media}")
    print(f"A mediana dos números {numeros} é: {mediana}")
    print(f"A moda dos números {numeros} é: {moda}")
lista_media()