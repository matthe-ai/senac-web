def cad_aluno():
    alunos = []
    while True:
        nome = input("Digite o nome do aluno ou sair para finalizar: ")
        if nome.lower() == "sair":
            break
        alunos.append(nome)
    print("Os alunos cadastrados foram: ")
    for i in range(len(alunos)):
        print(alunos[i])
cad_aluno()