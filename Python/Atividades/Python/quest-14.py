def classificador():
    numeros = []
    positivos = []
    negativos = []
    zero = []
    for i in range (6):
        n = int(input(f"Digite o {i+1}° número: "))
        numeros.append(n)
    for p in numeros:
        if p > 0:
            positivos.append(p)
        elif p < 0:
            negativos.append(p)
        else:
            zero.append(p)
    print(f"Números positivos: {positivos}, Números negativos: {negativos}, Quantidade de zeros: {len(zero)}")
classificador()