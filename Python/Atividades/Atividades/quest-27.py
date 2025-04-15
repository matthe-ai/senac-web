def senha_confirm():
    senha_1 = input("Digite sua senha: ")
    senha_2 = ""
    while senha_2 != senha_1:
        senha_2 = input("Confirme sua senha: ")
    print("Senha criada com sucesso")
senha_confirm()