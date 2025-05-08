import math

def calc_cient():
    numero = int(input("Digite um número: "))
    raiz = math.sqrt(numero)
    seno = math.sin(numero)
    cosseno = math.cos(numero)
    log = math.log(numero)
    print(f"A raiz de {numero} é: ", raiz)
    print(f"O seno de {numero} é: ", seno)
    print(f"O cosseno de {numero} é: ", cosseno)
    print(f"O logaritmo natural de {numero} é: ", log)
calc_cient()