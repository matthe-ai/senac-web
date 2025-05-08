import sqlite3

class ConexaoBanco:
    def __init__(self,nome_banco = "alunos.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class AlunoDAO(ConexaoBanco): # a classe AlunoDAO está herdando a ConexaoBanco (logo, ela não irá precisar de função construtora novamente)
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            idade INTEGER NOT NULL
            )
    ''')

    def inserir_aluno(self,nome,idade):
        self.cursor.execute('''
            INSERT INTO alunos (nome, idade) VALUES (?, ?)
    ''',(nome,idade))
        self.conexao.commit()
        print(f"Aluno {nome} inserido com sucesso!")
        
    def listar_alunos(self):
        self.cursor.execute('SELECT * FROM alunos')
        alunos = self.cursor.fetchall()
        print("Lista de alunos: ")
        for aluno in alunos:
            print(f"ID: {aluno[0]} - nome {aluno[1]} - idade {aluno[2]}")

def menu():
    dao = AlunoDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir aluno")
        print("2 - Listar alunos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            dao.inserir_aluno(nome,idade)
        elif opcao == "2":
            dao.listar_alunos()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Digite uma opção válida")
menu()