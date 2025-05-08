def Horas():
    hora = float(input("Quantas horas você trabalhou hoje ? "))
    valor = float(input("Quanto vale a sua hora ? "))
    total = hora * valor
    print(f"O total do seu dia foi {total}")
    if hora > 8:
        print("Hora extra registrada!")

Horas()