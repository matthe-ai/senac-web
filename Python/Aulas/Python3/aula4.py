import math

def raiz_quadrado():
    numero = float(input("Digite um número: "))
    raiz = math.sqrt(numero)
    potencia = math.pow(numero,2)

    print("A raiz quadrada do ",numero, "é: ", raiz)
    print("O quadrado do ",numero, "é: ", potencia)
raiz_quadrado()

import random

def aleatorio():
    print("Vamos sortear um número: ")
    numero = random.randint(1,100)
    print("O coisa gerado é: ", numero)
aleatorio()

from datetime import datetime

def hr_dt():
    agora = datetime.now()
    print("A data e hora de agora é: ", agora.strftime("%d/%m/%Y, %H:%M:%S"))
hr_dt()