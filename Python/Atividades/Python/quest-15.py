def name_a():
    name = []
    nomes_a = []
    for i in range (5):
        n = input(f"Digite o {i+1} nome: ").lower()
        name.append(n)
    for p in name:
        letra = p[0]
        if letra == "a":
            nomes_a.append(p)
    print(f"Estes nomes começam com 'A' {nomes_a}")
name_a()