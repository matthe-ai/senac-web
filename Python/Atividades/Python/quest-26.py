def soma(n1,n2):
    return (n1+n2)
def subtracao(n1,n2):
    return (n1-n2)
def multiplicacao(n1,n2):
    return (n1*n2)
def divisao(n1,n2):
    return (n1/n2)
def operacoes():
    operacao = ""
    while operacao != "sair":
        print("Qual das operações você deseja realizar ?")
        operacao = input("soma \nsubtração \nmultiplicação \ndivisão \n ").lower()
        if operacao == "soma":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"O resultado deu: {soma(n1,n2)}")
        elif operacao == "subtração":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"O resultado deu: {subtracao(n1,n2)}")
        elif operacao == "multiplicação":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"O resultado deu: {multiplicacao(n1,n2)}")
        elif operacao == "divisão":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            if n2 == 0:
                print("valor inválido")
            else:
                print(f"O resultado deu: {divisao(n1,n2)}")
        elif operacao != "sair":
            print("Operação inválida")
operacoes()