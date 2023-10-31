# Crie um programa que vai gerar cinco números aleatórios e colocar em uma Tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na Tupla

from random import randint

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(tupla)
tupla_ordenada = sorted(tupla)

print(f"O maior número gerado foi {tupla_ordenada[-1]}. \nE o menor foi {tupla_ordenada[0]}")