def vogais():
    vogais = ['a','e','i','o','u']
    vogais_found = []
    palavra = input("Digite uma palavra: ")
    for i in palavra:
        for p in range (5):
            if i == vogais[p]:
                vogais_found.append(i)
    print(f"Foram encontradas {len(vogais_found)} vogais")
vogais()