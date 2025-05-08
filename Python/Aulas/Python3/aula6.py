# Programação orientada a objetos e flask
'''
class Pessoa:
    def __init__(self, nome, idade): #self é obrigatorio e o que vier depois são as variaveis que você vai criar
        self.nome = nome # criei a variavel nome e atribui ela ao self.nome
        self.idade = idade # criei a variavel idade e atribui ela ao self.idade
    
    def apresentar(self): # toda função recebe um self
        print(f"Meu nome é {self.nome} e minha idade é {self.idade}")

p1 = Pessoa("Jorge",35) # criar um objeto Pessoa e atribuir à uma variavel
p2 = Pessoa("Alex",30)
p1.apresentar() # utilizando o objeto para chamar uma função da classe
p2.apresentar()



class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    
    def aplicar_desconto(self,porcentagem):
        desconto = self.preco*(porcentagem/100)
        self.preco -= desconto
    
    def mostrar_produto(self):
        print(f"{self.nome} custa R$ {self.preco:.2f}")
produto = Produto("Monitor",1200)
produto.mostrar_produto()
produto.aplicar_desconto(10)
produto.mostrar_produto()

'''

'''
# Fundamento de controle em POO

class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self,valor):
        self.saldo -= valor

    def exibir_saldo(self):
        print(f"O saldo do titular {self.titular} é R$ {self.saldo:.2f}")

conta = ContaBancaria("Luis", 0)
conta.exibir_saldo()
conta.depositar(200)
conta.exibir_saldo()
conta.sacar(100)
conta.exibir_saldo()
conta.sacar(800)
conta.exibir_saldo()
'''

class Aluno:
    def __init__(self,nome):
        self.nome = nome
        self.notas = []
    def adicionar_nota(self,nota):
        self.notas.append(nota)

    def calcular_nota(self):
        if self.notas:
            return sum(self.notas)/len(self.notas)
        else:
            return 0
        
    def exibir(self):
        media = self.calcular_nota()
        print(f"{self.nome} - Notas: {self.notas} - Media: {media:.2f}")

def menu_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome)
    while True:
        print("1 - Adicionar nota")
        print("2 - Exibir dados do aluno")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nota = float(input("Digite a nota: "))
            aluno.adicionar_nota(nota)
        elif opcao == "2":
            aluno.exibir()
        elif opcao == "3":
            break
        else:
            print("Digite uma opção válida")
menu_aluno()