def horas():
    #hora
    hora = int(input("Quantas horas você quer conte ?  "))
    for h in range(hora):
        #minuto
        for m in range(60):
            #segundos
            for s in range(60):
                print(f"{h} horas, {m} minutos e {s} segundos")
horas()