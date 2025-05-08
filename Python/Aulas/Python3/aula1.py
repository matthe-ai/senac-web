'''
inteiros = int
palavras/letras = str
fracionario = float
'''

def bom_dia():
    print("Olá mundo")

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo ao mundo do Python")

# nome = input("Diga seu nome: ")

def soma():
    print(2+2)

def multiplicacao(num1,num2):
    print(num1*num2)

def subtracao(num1,num2):
    print(num1-num2)

def divisao(num1,num2):
    print(num1/num2)

a = int(input("Digite o primeiro numero que você quer: "))
b = int(input("Digite o segundo numero que você quer: "))

soma()
multiplicacao(a,b)
subtracao(a,b)
divisao(a,b)