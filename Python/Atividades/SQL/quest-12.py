import sqlite3

class ConexaoBanco:
    def __init__(self,nome_banco="xadrez.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    
    def fechar(self):
        self.cursor.close()
class XadrezDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS xadrez(nome TEXT NOT NULL,pontuacao INTEGER NOT NULL)''')
    def inserir_dados(self,nome,pontuacao):
        self.cursor.execute('''INSERT INTO xadrez (nome,pontuacao) VALUES (?,?)''',(nome,pontuacao))
        self.conexao.commit()
    def buscar_dados(self,pontuacao_min):
        self.cursor.execute('SELECT * FROM xadrez WHERE pontuacao >= (?)',(pontuacao_min,))
        alunos = self.cursor.fetchall()
        for aluno in alunos:
            print(f"Aluno {aluno[0]} - Pontuação {aluno[1]}")

def menu():
    dao = XadrezDAO()
    dao.criar_tabela()
    while True:
        print("1 - Adicionar aluno")
        print("2 - Listar alunos com pontuação minima à: ")
        print("3 - Sair")
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            pontuacao = int(input("Digite a pontuação do aluno: "))
            dao.inserir_dados(nome,pontuacao)
        elif opcao == "2":
            pontuacao = int(input("Digite a pontuação minima: "))
            dao.buscar_dados(pontuacao)
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Digite uma opção válida")
menu()