import time

def menu():
    tarefas = []
    while True:
        opcao = input("Digite o número do que você quer fazer: \n*** [1] Adicionar tarefa \n*** [2] Listar tarefas \n*** [3] Remover tarefa(por nome) \n*** [4] Sair \n*** Opção: ")
        if opcao == "1":
            tarefas.append(input("Digite o nome da tarefa: "))
        elif opcao == "2":
            print(f"As tarefas adicionadas até agora foram: ")
            for i in range(len(tarefas)):
                print(f"{i+1}° tarefa: {tarefas[i]}")
                time.sleep(.5)
        elif opcao == "3":
            remover = input("Digite a tarefa que você quer remover: ")
            try:
                tarefas.remove(remover)
            except ValueError:
                print("Tarefa não encontrada")
        elif opcao == "4":
            break
        else:
            print("Digite um número válido: ")
        time.sleep(1)
menu()