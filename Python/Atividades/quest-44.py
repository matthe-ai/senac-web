def notas_alunos():
    alunos = {}
    qntd = int(input("Quantos alunos serão cadastrados ? "))
    for i in range (qntd):
        nome = input(f"Digite o nome do {i+1}° aluno: ")
        nota_1 = 0
        for p in range (4):
            nota = float(input(f"Digite a {p+1}° nota do {nome}: "))
            nota_1 += nota
            media = nota_1/4
        alunos[nome] = media
    # media individual
    aprovados = 0
    for aluno in alunos.keys():
        print(f"A media do(a) {aluno} foi {alunos[aluno]:.2f}")
        if alunos[aluno] >= 7:
            aprovados += 1
    # media da turma
    nota_turma = 0
    for notas in alunos.values():
        nota_turma += notas
    media_turma = nota_turma/qntd
    print(f"A média geral da turma foi {media_turma:.2f} e a quantidade de aprovados foi de: {aprovados}")
notas_alunos()