def caixa():
    notas_d = [100,50,20,10]
    valor = int(input("Digite o valor que você deseja retirar: "))
    notas_t = {}
    if valor < 0 or valor % 10 != 0:
        print("Valor inválido")
        caixa()
    for i in notas_d:
        valor_n = valor//i
        valor_r = valor%i
        valor = valor_r
        notas_t[i] = valor_n
    print(f"Você vai sacar {notas_t[100]} nota(s) de 100, {notas_t[50]} nota(s) de 50, {notas_t[20]} nota(s) de 20 e {notas_t[10]} nota(s) de 10")
    if valor_r < 10 and valor_r != 0:
        print(f"Mas não foi possivel fornecer esse valor: {valor_r}")
caixa()