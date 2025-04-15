# Caixa eletronico
valor_o = int(input("Digite o valor: "))
def n100(valor):
    n100 = valor//100
    valor = valor - n100*100
    return n100, valor
def n50(valor):
    n50 = valor//50
    valor = valor - n50*50
    return n50, valor
def n20(valor):
    n20 = valor//20
    valor = valor - n20*20
    return n20, valor
def n10(valor):
    n10 = valor//10
    valor=valor-n10*10
    return n10, valor
def caixa(valor):
    if valor >= 100:
        a100, valor_f1 = n100(valor)
        if valor_f1 >= 50:
            a50, valor_f2 = n50(valor_f1)
            if valor_f2 >=20:
                a20, valor_f3=n20(valor_f2)
                if valor_f3 >=10:
                    a10, valor_f4=n10(valor_f3)
                    print(f"{a100} notas de 100, {a50} notas de 50, {a20} notas de 20 e {a10} notas de 10")
                    if valor_f4 != 0:
                        print(f"Mas não foi temos notas de {valor_f4}")
                else:
                    print(f"{a100} notas de 100, {a50} notas de 50 e {a20} notas de 20")
                    if valor_f3 != 0:
                        print(f"Mas não foi temos notas de {valor_f4}")
            elif valor_f2 >=10:
                a10,valor_f3=n10(valor_f2)
                print(f"{a100} notas de 100, {a50} notas de 50 e {a10} notas de 10")
                if valor_f3 != 0:
                    print(f"Mas não foi temos notas de {valor_f3}")
            else:
                print(f"{a100} notas de 100 e {a50} notas de 50")
                if valor_f2 != 0:
                    print(f"Mas não foi temos notas de {valor_f2}")
        elif valor_f1 >=20:
            a20, valor_f3=n20(valor_f1)
            if valor_f3 >=10:
                a10, valor_f4=n10(valor_f3)
                print(f"{a100} notas de 100, {a20} notas de 20 e {a10} notas de 10")
                if valor_f4 != 0:
                    print(f"Mas não foi temos notas de {valor_f4}")
            else:
                print(f"{a100} notas de 100 e {a20} notas de 20")
                if valor_f3 != 0:
                    print(f"Mas não foi temos notas de {valor_f3}")
        elif valor_f1 >=10:
            a10, valor_f2=n10(valor_f1)
            print(f"{a100} notas de 100 e {a10} notas de 10")
            if valor_f2 != 0:
                print(f"Mas não foi temos notas de {valor_f2}")
        else:
            print(f"{a100} notas de 100")
            if valor_f1 != 0:
                print(f"Mas não foi temos notas de {valor_f1}")
    elif valor >= 50:
        a50, valor_f1=n50(valor)
        if valor_f1>= 20:
            a20,valor_f2=n20(valor_f1)
            if valor_f2 >= 10:
                a10,valor_f3=n10(valor_f2)
                print(f"{a50} notas de 50, {a20} notas de 20 e {a10} notas de 10")
                if valor_f3 != 0:
                    print(f"Mas não foi temos notas de {valor_f3}")
            else:
                print(f"{a50} notas de 50 e {a20} notas de 20")
                if valor_f2 != 0:
                    print(f"Mas não foi temos notas de {valor_f2}")
        else:
            print(f"{a50} notas de 50")
            if valor_f1 != 0:
                print(f"Mas não foi temos notas de {valor_f1}")
    elif valor >= 20:
        a20, valor_f1=n20(valor)
        if valor_f1 >= 10:
            a10, valor_f2=n10(valor_f1)
            print(f"{a20} notas de 20 e {a10} notas de 10")
            if valor_f2 != 0:
                print(f"Mas não foi temos notas de {valor_f2}")
        else:
            print(f"{a20} notas de 20")
            if valor_f1 != 0:
                print(f"Mas não foi temos notas de {valor_f1}")
    elif valor >= 10:
        a10, valor_f1=n10(valor)
        print(f"{a10} notas de 10")
        if valor_f1 != 0:
            print(f"Mas não foi temos notas de {valor_f1}")
    else:
        print(f"Não foi temos notas de {valor}")
caixa(valor_o)