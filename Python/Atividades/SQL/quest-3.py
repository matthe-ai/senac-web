import sqlite3

class ConexaoBanco:
    def __init__(self,nome_banco = "professores.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    
    def fechar(self):
        self.cursor.close()

class ProfessorDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS professores(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            disciplina TEXT NOT NULL)
            ''')
    def inserir_dados(self,nome,disciplina):
        self.cursor.execute('''INSERT INTO professores (nome,disciplina) VALUES (?,?)''',(nome,disciplina))
        self.conexao.commit()
    def listar_dados(self):
        self.cursor.execute('SELECT * FROM professores')
        disciplinas = self.cursor.fetchall()
        for disciplina in disciplinas:
            print(f"{disciplina[1]} ministra {disciplina[2]}")

def menu():
    dao = ProfessorDAO()
    dao.criar_tabela()

    while True:
        print("1 - Adicionar professor")
        print("2 - Listar professores")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do professor: ")
            disciplina = input("Digite a disciplina que ele ensina: ")
            dao.inserir_dados(nome,disciplina)
        elif opcao == "2":
            dao.listar_dados()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Digite uma opção válida")
menu()