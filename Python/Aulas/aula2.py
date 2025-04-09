def soma(i1,i2):
    resultado = i1+i2
    return resultado
# i1 = int(input("Numero 1: "))
# i2 = int(input("Numero 2: "))
# print(soma(i1,i2))

# calculadora

def calculadora():
    print("Escolha a operação")
    op = input("Soma Subtração Divisão Multiplicação: ").lower()
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    if op == "soma":
        print(f"Resultado: {n1+n2}")
    elif op == "subtração":
        print(f"Resultado: {n1-n2}")
    elif op == "divisão":
        if n2 != 0:
            print(f"Resultado: {n1/n2}")
        else:
            print("Divisão por 0 é indefinido")
    else:
        print(f"Resultado: {n1*n2}")

calculadora()