idade = int(input("Idade: "))
nome = input("Nome: ")
genero = input("Gênero: ")

class Person:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def eh_maior_de_idade(self):
        return self.idade >= 18
    
    def incrementa_idade(self):
        self.idade = self.idade + 1

    def vembalizar(self):
        self.nome = "Vemba"
    
    def __str__(self):
        return "{}, {}, tem {} anos de idade".format(self.nome, self.genero, self.idade)

pessoa = Person(nome, idade, genero)
godoy = Person("Godoy", 15, "Helicopter")

pessoa.nome



print(pessoa.idade)
pessoa.incrementa_idade()
print(pessoa.idade)
print(pessoa.nome)
pessoa.vembalizar()
print(pessoa.nome)