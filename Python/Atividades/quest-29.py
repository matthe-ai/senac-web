def adivinha():
    numero_s = 7
    for i in range (3):
        numero_u = int(input("Digite um número: "))
        if numero_u == numero_s:
            print("Parabéns")
            break
        elif numero_u > numero_s:
            if i == 2:
                print("Suas chances acabaram")
                break
            print("Menor")
        elif numero_u < numero_s:
            if i == 2:
                print("Suas chances acabaram")
                break
            print("Maior")
adivinha()