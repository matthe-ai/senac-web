import random

def senha():
    algarismos = ['0','1','2','3','4','5','6','7','8','9']
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '^', '~', '@', '-', '_', 'ç', 'Ç','`', '/', '|', 'ª', 'º', '¿']
    
    senha = []

    n_algarismo = random.randint(1,5)
    n_letras = random.randint(1, 5)
    n_simbolo = 10-n_algarismo-n_letras
    for i in range (n_algarismo):
        n = random.choice(algarismos)
        senha.append(n)
        n = ""
    for j in range (n_letras):
        m = random.choice(letras)
        senha.append(m)
        m = ""
    for q in range (n_simbolo):
        p = random.choice(simbolos)
        senha.append(p)
        p = ""
    random.shuffle(senha)

    senha_text = ""
    for caracter in senha:
        senha_text += caracter

    print(f"Sua senha é {senha_text}")
senha()