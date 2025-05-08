import sqlite3

class ConexaoBanco:
    def __init__(self,nome_banco = "cursos.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    
    def fechar(self):
        self.conexao.close()

class CursoDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cursos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            nivel TEXT NOT NULL)
        ''')

    def inserir_dados(self,nome,nivel):
        self.cursor.execute('''
            INSERT INTO cursos (nome,nivel) VALUES (?,?)
        ''',(nome,nivel))
        self.conexao.commit()
        print("Cadastrado!")

    def listar_dados(self):
        self.cursor.execute('SELECT * FROM cursos')
        cursos = self.cursor.fetchall()
        print("Lista de cursos: ")
        for curso in cursos:
            print(f"O curso {curso[1]} possui a dificuldade {curso[2]}.")

def menu():
    dao = CursoDAO()
    dao.criar_tabela()

    while True:
        print("1 - Adicionar curso e nivel")
        print("2 - Listar cursos")
        print("3 - Sair")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            curso = input("Digite o nome do curso: ")
            nivel = input("Digite o nivel do curso: (iniciante) (intermediario) (avançado) \nEscolha: ").lower()
            if nivel == "iniciante" or nivel == "intermediario" or nivel == "avançado":
                dao.inserir_dados(curso,nivel)
            else:
                print("Nivel de dificuldade inválido")
        elif opcao == "2":
            dao.listar_dados()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Opção inválida")
menu()