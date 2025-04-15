def cadastro():
    nomes = []
    while True:
        nome = input("Digite o nome do aluno para cadastrar ele: ")
        if nome == "sair":
            break
        nomes.append(nome)
    print(f"Foram cadastrados {len(nomes)}, veja os nomes a seguir: {nomes}")
cadastro()