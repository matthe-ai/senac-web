def tabuada():
    resp = 0
    while resp != "nao":
        numero = int(input("Digite o número que você quer a tabuada até o 10: "))
        for i in range(1, 11):
            print(f"{i} x {numero} = {i*numero}")
            if i == 10:
                resp = input("Você quer calcular novamente ? (sim) (nao) ")
tabuada()