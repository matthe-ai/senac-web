def notas():
    soma = 0
    for i in range (5):
        nota = float(input(f"Digite a {i+1}° nota: "))
        soma += nota
    media = soma/5
    if media >= 7:
        print("Aprovado")
    elif media < 5:
        print("Reprovado")
    else:
        print("Recuperação")
notas()