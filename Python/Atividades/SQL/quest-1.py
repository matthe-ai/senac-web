import sqlite3

class ConexaoBanco:
    def __init__(self,nome_banco = "livros.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class LivroDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            autor TEXT NOT NULL
                            )
        ''')
    
    def inserir_livro(self,titulo,autor):
        self.cursor.execute('''
            INSERT INTO livros (titulo,autor) VALUES (?,?)
        ''',(titulo,autor))
        self.conexao.commit()
        print("Cadastrado!")
    
    def listar(self):
        self.cursor.execute('SELECT * FROM livros')
        livros = self.cursor.fetchall()
        print("Lista de livros: ")
        for livro in livros:
            print(f"Titulo: {livro[1]} Autor: {livro[2]}")
def menu():
    dao = LivroDAO()
    dao.criar_tabela()

    while True:
        print("1 - Adicionar livro e autor")
        print("2 - Listar livro e autor")
        print("3 - Sair")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            dao.inserir_livro(titulo,autor)
        elif opcao == "2":
            dao.listar()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Opção inválida")
menu()