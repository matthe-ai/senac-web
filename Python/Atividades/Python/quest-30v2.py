def dados_palavras():
    palavras = []
    vogais = ['a','e','i','o','u']
    espaco = " "
    vogal = {}
    consoante = {}
    espacos = {}
    for i in range(3):
        palavras.append(input(f"Digite a {i+1}° palavra: "))
    for palavra in palavras:
        num_vogal = 0
        num_consoante = 0
        num_espaco = 0
        for letra in palavra:
            if letra.lower() in vogais:
                num_vogal += 1
            elif letra.lower() in espaco:
                num_espaco += 1
            elif letra.lower().isalpha():
                num_consoante += 1
        vogal[palavra] = num_vogal
        consoante[palavra] = num_consoante
        espacos[palavra] = num_espaco
    for d in range(3):
        print(f"A palavra {palavras[d]} possui {vogal[palavras[d]]} vogais, {consoante[palavras[d]]} consoantes e {espacos[palavras[d]]} espaços")
dados_palavras()