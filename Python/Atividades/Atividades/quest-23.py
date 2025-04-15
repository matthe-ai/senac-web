def num_primo():
    num = -1
    num_f = 0
    while num != 0:
        num = int(input("Digite um número: "))
        if num == 0:
            break
        else:
            for i in range(1,(num+1)):
                if num%i == 0:
                    num_f += i
            if num_f > (num+1):
                print("Este número não é primo")
            else:
                print("Este número é primo")
            num_f = 0
num_primo()