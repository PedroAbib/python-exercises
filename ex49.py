# Refaça o Desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input("Digite um número: "))

for tabuada in range(1, 11):
    print("{} x {} = {}".format(numero, tabuada, numero * tabuada))
