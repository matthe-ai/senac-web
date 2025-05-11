import sqlite3

class ConexaoBanco:
    def __init__(self,nome_banco="camisetas.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    
    def fechar(self):
        self.cursor.close()
class CamisetasDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS camisetas(nome TEXT NOT NULL, cor TEXT NOT NULL, quantidade INTEGER NOT NULL)''')
    def inserir_dados(self,nome,cor,quantidade):
        self.cursor.execute('''INSERT INTO camisetas (nome,cor,quantidade) VALUES (?,?,?)''',(nome,cor,quantidade))
        self.conexao.commit()
    def atualizar_quantidade(self,nome,nova_quantidade):
        self.cursor.execute('UPDATE camisetas SET quantidade = ? WHERE nome = ?',(nova_quantidade,nome))
        self.conexao.commit()
    def listar_dados(self):
        self.cursor.execute('SELECT * FROM camisetas')
        camisas = self.cursor.fetchall()
        for camisa in camisas:
            print(f"A camisa do modelo {camisa[0]} e cor {camisa[1]} possui {camisa[2]} unidades")

def menu():
    dao = CamisetasDAO()
    dao.criar_tabela()
    while True:
        print("1 - Adicionar camisa")
        print("2 - Listar camisas")
        print("3 - Atualizar quantidade")
        print("4 - Sair")
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            nome = input("Digite o modelo da camisa: ")
            cor = input("Digite a cor da camisa: ")
            quantidade = int(input("Digite a quantidade de camisas disponiveis: "))
            dao.inserir_dados(nome,cor,quantidade)
        elif opcao == "2":
            dao.listar_dados()
        elif opcao == "3":
            nome = input("Digite o modelo de camisa a ser atualizado: ")
            nova_quantidade = int(input("Digite a nova quantidade disponivel dessa camisa: "))
            dao.atualizar_quantidade(nome,nova_quantidade)
        elif opcao == "4":
            dao.fechar()
            break
        else:
            print("Digite uma opção válida")
menu()