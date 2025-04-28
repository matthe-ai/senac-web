# Dicionario


def frutas():
    fruta = {"maçã","banana","laranja","uva"}
    print("Minhas frutas: ")
    for f in fruta:
        print(f"- {f}")
frutas()


def lista_produto():
    produtos = {
        "notebook": 3500.00,
        "chinelo": 50.00,
        "maçã": 8.5
    }
    print("Meus produtors: ")
    for produto in produtos.keys():
        print(f"- {produto}")
lista_produto()


def produtos_mais():
    produtos = {
        "notebook":("LG","3500.00","cartão em até 12x com acréscimo"),
        "monitor":("Samsung","1400.00","cartão em 6x sem juros"),
        "Teclado":("Logitech","122.00","A vista")
    }

    print("Produtos cadastrados: ")
    for produto, detalhes in produtos.items():
        marca, preco, pagamento = detalhes
        print(f"Produto: {produto}")
        print(f"Marca: {marca}")
        print(f"Preço: {preco}")
        print(f"Pagamento: {pagamento}\n")
produtos_mais()