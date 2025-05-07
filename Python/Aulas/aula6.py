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

'''

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