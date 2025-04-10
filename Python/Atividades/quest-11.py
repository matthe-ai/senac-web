def votos():
    ana = 0
    bruno = 0
    carla = 0
    for i in range(6):
        voto = input("1 para Ana, 2 para Bruno e 3 para Carla: ")
        if voto == "1":
            ana += 1
        elif voto == "2":
            bruno += 1
        elif voto == "3":
            carla += 1
        else:
            print("Você votou em alguém inválido")
    print(f"Ana tirou {ana} votos, Bruno tirou {bruno} votos e Carla tirou {carla} votos.")
votos()