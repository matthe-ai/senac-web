print("Descubra se você foi aprovado já")
def media():
    n1 = float(input("Qual a sua primeira nota ? "))
    n2 = float(input("Qual a sua segunda nota ? "))
    n3 = float(input("Qual a sua terceira nota ? "))
    media = (n1+n2+n3)/3
    return media

media_3 = media()

def aprovado(media):
    if media >= 7:
        print("Aprovado")
    elif media < 7 and media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

aprovado(media_3)