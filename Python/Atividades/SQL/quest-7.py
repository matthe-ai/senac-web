import sqlite3
class ConexaoBanco:
    def __init__(self,nome_banco = "lanches.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.cursor.close()
class LanchesDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS lanches(
                            nome TEXT NOT NULL,
                            preco FLOAT NOT NULL)''')
    def adicionar_lanche(self,nome,preco):
        self.cursor.execute('''INSERT INTO lanches (nome,preco) VALUES (?,?)''',(nome,preco))
        self.conexao.commit()
    def listar_lanche(self):
        self.cursor.execute('SELECT * FROM lanches')
        lanches = self.cursor.fetchall()
        for lanche in lanches:
            print(f"* {lanche[0]} custa R$ {lanche[1]:.2f}")
def menu():
    dao = LanchesDAO()
    dao.criar_tabela()
    while True:
        print("1 - Adicionar lanche")
        print("2 - Listar lanches")
        print("3 - Sair")
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do lanche: ")
            valor = input("Digite o valor do lanche: ")
            dao.inserir_lanche(nome,valor)
        elif opcao == "2":
            dao.listar_lanche()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Digite uma opção válida")
menu()