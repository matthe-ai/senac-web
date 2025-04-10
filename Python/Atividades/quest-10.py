#calculadora de imc

def IMC(peso, altura):
    imc = peso/(altura*altura)
    print(imc)
    if imc >= 30:
        print("Obesidade")
    elif imc < 30 and imc >= 25:
        print("Sobrepeso")
    elif imc < 25 and imc >= 18.5:
        print("Peso normal")
    else:
        print("Abaixo do peso")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))

IMC(peso, altura)