'''
quest 1
Resposta: B
'''

'''
quest 2
Resposta: C
'''

'''
quest 3
Resposta: Olá, Lucas
'''

'''
quest 4
Resposta: C
'''

'''
quest 5
Resposta:

class Aluno:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def mostrar_idade(self):
        print(f"A idade do aluno {self.nome} é {self.idade}")
'''

'''
quest 6
Resposta: B
'''

'''
quest 7
Resposta:

class Produto:
    def __init__(self,produto,valor):
        self.produto = produto
        self.valor = valor
    def desconto(self):
        self.valor *= 0.9
'''

'''
quest 8
Resposta: B
'''

'''
quest 9
Resposta: 12.56
'''

'''
quest 10
Resposta: 

Atributo é algo necessario ja especificado dentro da função __init__ enquanto o método é uma função que irá utilizar o atributo

class Estado():
    def __init__(self,cidade): #atributo cidade está sendo requisitado na função construtora
        self.cidade = cidade
        self.cidades = []
    def adicionar_cidade(self): #metodo para adicionar a cidade à uma lista
        self.cidades.append(self.cidade)
'''