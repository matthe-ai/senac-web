def paises():
    paises = {"Brasil", "Argentina", "Colômbia", "Peru", "Venezuela", "Chile"}
    for i in range(3):
        pais = input("Digite o nome de um país: ").capitalize()
        if pais in paises:
            print("Sim, esse país está presente na lista!")
        else:
            print("Não, esse país não está presente na lista!")
paises()