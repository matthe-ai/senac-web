import sqlite3

class ConexaoBanco:
    def __init__(self,nome_banco="visitantes.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.cursor.close()

class VisitanteDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS visitante(
                            nome TEXT NOT NULL,
                            motivo TEXT NOT NULL)''')
    def inserir_visitante(self,nome,motivo):
        self.cursor.execute('''INSERT INTO visitante (nome,motivo) VALUES (?,?)''',(nome,motivo))
        self.conexao.commit()
    def remover_visitante(self,nome):
        self.cursor.execute('DELETE FROM visitante WHERE nome = ?',[nome])
        self.conexao.commit()
    def listar_visitante(self):
        self.cursor.execute('SELECT * FROM visitante')
        visitantes = self.cursor.fetchall()
        for visitante in visitantes:
            print(f"O visitante {visitante[0]} está presente pelo motivo {visitante[1]}")

def menu():
    dao = VisitanteDAO()
    dao.criar_tabela()
    while True:
        print("1 - Adicionar visitante")
        print("2 - Listar visitantes")
        print("3 - Remover visitante")
        print("4 - Sair")
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do visitante: ")
            motivo = input("Digite o motivo da visita: ")
            dao.inserir_visitante(nome,motivo)
        elif opcao == "2":
            dao.listar_visitante()
        elif opcao == "3":
            remove_visitante = input("Digite o nome do visitante: ")
            dao.remover_visitante(remove_visitante)
        elif opcao == "4":
            dao.fechar()
            break
        else:
            print("Digite uma opção válida")
menu()