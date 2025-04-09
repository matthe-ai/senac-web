def VerSenha():
    senha = "senac123"
    senha_user = input("Digite sua senha: ")
    if senha == senha_user:
        print("Pode continuar")
    else:
        print("Senha incorreta!")
VerSenha()