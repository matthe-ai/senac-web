def senha():
    senha = "senac123"
    user = ""
    while user != senha:
        user = input("Digite sua senha: ")
        if user == senha:
            print("Acesso liberado")
            break
senha()