def cursos():
    cursos_manha = {"portugues","matematica","historia","geografia","ciencias"}
    cursos_noite = {"ingles","artes","portugues","filosofia","geografia"}
    resp = input("Qual horario você quer consultar: (manha) (noite) (ambos) \nEscolha: ").lower()
    if resp == "manha":
        print("Estes cursos estão disponiveis apenas de manhã: ")
        for manha in cursos_manha:
            print(f"- {manha}")
    elif resp == "noite":
        print("Estes cursos estão disponiveis apenas de noite: ")
        for noite in cursos_noite:
            print(f"- {noite}")
    elif resp == "ambos":
        print("Estes cursos estão disponiveis em ambos os horarios: ")
        ambos = cursos_manha.intersection(cursos_noite)
        for manha_noite in ambos:
            print(f"- {manha_noite}")
    else:
        print("Escolha uma alternativa disponivel")
        cursos()
cursos()