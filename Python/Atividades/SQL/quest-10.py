import sqlite3

class ConexaoBanco:
    def __init__(self,nome_banco="clube_leitura.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    
    def fechar(self):
        self.cursor.close()
class LivroDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS livros(
                            id INTEGER PRIMARY KET AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            autor TEXT NOT NULL)''')
    def inserir_livros(self,titulo,autor):
        self.cursor.execute('''INSERT INTO livros (titulo,autor) VALUES (?,?)''',(titulo,autor))
        self.conexao.commit()
    def buscar_por_titulo(self,titulo):
        self.cursor.execute('SELECT * FROM livros WHERE titulo = ?',[titulo])
        livro = self.cursor.fetchall()
        if livro:
            print(f"O livro {livro[1]} foi encontrado e seu autor é o(a) {livro[2]}.")
        else:
            print(f"O livro {livro[1]} não foi encontrado.")
    
def menu():
    dao = LivroDAO()
    dao.criar_tabela()

    while True:
        titulo = ""
        autor = ""
        print("1 - Adicionar livro")
        print("2 - Buscar livro")
        print("3 - Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            titulo = input("Digite o titulo do livro: ")
            autor = input("Digite o autor do livro: ")
            dao.inserir_livros(titulo,autor)
        elif opcao == "2":
            titulo = input("Digite o titulo do livro que você deseja procurar: ")
            dao.buscar_por_titulo(titulo)
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Digite uma opção válida!")
menu()