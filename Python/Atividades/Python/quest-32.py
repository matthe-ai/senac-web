import random

def dado():
    numero = random.randint(1,6)
    print("O resultado do lançamento do dado é: ", numero)
    dnv = input("Voce quer jogar de novo ? (s) (n) ")
    if dnv.lower() == "s":
        dado()
dado()