import sqlite3

class ConexaoBanco:
    def __init__(self,nome_banco="gamer.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    
    def fechar(self):
        self.cursor.close()

class EstacaoGamer(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS gamer(
                            produto TEXT NOT NULL,
                            valor FLOAT NOT NULL)''')
    def inserir_produto(self,produto,valor):
        self.cursor.execute('''INSERT INTO gamer (produto,valor) VALUES (?,?)''',(produto,valor))
        self.conexao.commit()
    def atualizar_preco(self,produto,novo_valor):
        self.cursor.execute('UPDATE gamer SET valor = ? WHERE produto = ?',(novo_valor,produto))
        self.conexao.commit()
    def listar_produto(self):
        self.cursor.execute('SELECT * FROM gamer')
        produtos = self.cursor.fetchall()
        for produto in produtos:
            print(f"Produto: {produto[0]} - Preço: {produto[1]}")

def menu():
    dao = EstacaoGamer()
    dao.criar_tabela()
    while True:
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar valor")
        print("4 - Sair")
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            valor = input("Digite o valor do produto: ")
            dao.inserir_produto(nome,valor)
        elif opcao == "2":
            dao.listar_produto()
        elif opcao == "3":
            produto = input("Digite o nome do produto: ")
            valor_atualizado = float(input("Digite o valor atualizado do produto: "))
            dao.atualizar_preco(produto,valor_atualizado)
        elif opcao == "4":
            dao.fechar()
            break
        else:
            print("Digite uma opção válida")
menu()