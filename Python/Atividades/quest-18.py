def senha():
    senha = "senac123"
    user = 0
    while user != senha:
        user = input("Digite sua senha: ")
        if user == senha:
            print("Acesso liberado")
            break
senha()