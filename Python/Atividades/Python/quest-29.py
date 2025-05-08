def adivinha():
    numero_s = 7
    for i in range (3):
        numero_u = int(input("Digite um número: "))
        if numero_u == numero_s:
            print("Parabéns")
            break
        if i == 2:
            print("Suas chances acabaram")
            break
        elif numero_u > numero_s:
            print("Menor")
        elif numero_u < numero_s:
            print("Maior")
adivinha()