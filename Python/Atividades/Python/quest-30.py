def dados_palavra():
    palavras = []
    vogal = ['a','e','i','o','u']
    vogais = {}
    consoantes = {}
    espaco = {}
    # pedir as palavras
    for i in range (3):
        palavra = input(f"Digite a {i+1}° palavra: ").lower()
        palavras.append(palavra)
    # analisar cada palavra
    for p in palavras:
        vogal_p = 0
        espaco_p = 0
        consoante_p = 0
        #analisar cada caractere
        for k in p:
            for l in range (5):
                if k == vogal[l]:
                    vogal_p += 1
                elif k != vogal[l]:
                    if p == " ":
                        espaco_p += 1
                    elif k != "a" and k != "e" and k != "i" and k != "o" and k != "u":
                        consoante_p +=1
                        break
        vogais[p] = vogal_p
        consoantes[p] = consoante_p
        espaco[p] = espaco_p
    for m in range (3):
        print(f"A palavra {palavras[m]} possui {vogais[palavras[m]]} vogais, {consoantes[palavras[m]]} consoantes e {espaco[palavras[m]]} espaços")
dados_palavra()