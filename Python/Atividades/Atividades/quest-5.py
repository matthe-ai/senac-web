def temperatura():
    temp = float(input("Quantos graus está ai: "))
    if temp > 25:
        print("Que calor!")
    elif temp < 18:
        print("Que frio!")
    else:
        print("Agradável")
temperatura()