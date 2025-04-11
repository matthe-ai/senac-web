def desconto_caixa():
    valor = 0
    for i in range (4):
        n = float(input(f"Qual o valor do {i+1}° objeto: "))
        valor += n
    if valor > 200:
        print(f"Você recebeu um desconto de 10%, totalizando assim {valor*0.9}")
    elif valor < 100:
        print("Você não tem direito a um disconto, compre mais")
    else:
        print(f"Você recebeu um desconto de 5%, totalizando assim {valor*0.95}")
desconto_caixa()