def sum_pares():
    numeros = []
    pares = 0
    for i in range(6):
        numero = int(input("Digite um número: "))
        numeros.append(numero)
    for j in numeros:
        if j % 2 == 0:
            pares += j
    print(f"A soma dos números pares deu: {pares}")
sum_pares()