def proc_nome():
    nomes = ['jorge','luis','gustavo','daniel','arthur']
    nome = input("Digite um nome: ")
    presente = ""
    for i in nomes:
        if nome == i:
            presente = "sim"
    if presente == "sim":
        print("O nome está presente na lista")
    else:
        print("O nome não está presente na lista")
proc_nome()