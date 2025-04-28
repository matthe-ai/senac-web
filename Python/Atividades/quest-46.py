def cidades():
    cidades = set()
    for i in range(8):
        cidades.add(input(f"Digite o nome da {i+1}° cidade: "))
    print(f"Foram cadastradas {len(cidades)} cidades")
    print("Veja as cidades cadastradas abaixo: ")
    for cidade in cidades:
        print(f"- {cidade}")
cidades()