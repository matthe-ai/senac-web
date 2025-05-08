def multiplos():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    for i in [n1]:
        if n1 % n2 == 0:
            print(f"{n1} é multiplo de {n2}")
        else:
            print(f"{n1} não é multiplo de {n2}")
multiplos()