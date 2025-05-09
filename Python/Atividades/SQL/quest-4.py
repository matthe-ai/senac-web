import sqlite3
class ConexaoBanco:
    def __init__(self,nome_banco="clientes.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.cursor.close()
class ClienteDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL)
                ''')
    def inserir_cliente(self,nome,email):
        self.cursor.execute('''INSERT INTO clientes (nome,email) VALUES (?,?)''',(nome,email))
        self.conexao.commit()
    def listar_cliente(self):
        self.cursor.execute('SELECT * FROM clientes')
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(f"O cliente {cliente[1]} possui o email {cliente[2]}")
def menu():
    dao = ClienteDAO()
    dao.criar_tabela()
    while True:
        print("1 - Adicionar cliente")
        print("2 - Listar clientes")
        print("3 - Sair")
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            dao.inserir_cliente(nome,email)
        elif opcao == "2":
            dao.listar_cliente()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Digite uma opção válida")
menu()