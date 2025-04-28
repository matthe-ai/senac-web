def produtos():
    produtos = {}
    media = 0
    for i in range(3):
        nome = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: "))
        produtos[nome] = valor
        media += valor
    print("Produtos cadastrados: \n")
    for produto in produtos:
        print(f"Produto: {produto}, Valor: {produtos[produto]}")
    media = media/len(produtos.values())
    print(f"A media de valores foi {media:.2f}")
produtos()