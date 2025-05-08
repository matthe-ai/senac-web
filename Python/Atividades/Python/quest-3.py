print("Descubra se você passou de ano com este programa")

def nota():
    nota = float(input("Digite a nota que você tirou: "))
    if nota >= 7:
        print("Aprovado")
    elif nota < 7 and nota >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

nota()