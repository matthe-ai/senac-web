def combustivel():
    print("Qual combustivel você quer colocar:")
    tipo = int(input("1 - Gasolina \n2 - Diesel \n3 - Álcool \n"))
    gasolina = 5.59
    alcool = 4.39
    diesel = 5.99
    if tipo == 1:
        tipo = "gasolina"
    elif tipo == 2:
        tipo = "diesel"
    else:
        tipo == "alcool"
    litros = float(input(f"Quantos litros você quer de {tipo} ? "))
    if tipo == "gasolina":
        print(f"O total deu: R${gasolina*litros}")
    elif tipo == "diesel":
        print(f"O total deu: R${diesel*litros}")
    else:
        print(f"O total deu: R${alcool*litros}")
    resp = input("Você deseja calcular mais um combustivel ? (S) (N) ").lower()
    if resp == "sim":
        combustivel()
combustivel()