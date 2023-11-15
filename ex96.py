# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.

def area(l, c):
    print(f'A área é {l * c}m².')

l = float(input("Largura(m): "))
c = float(input("Comprimento(m): "))
area(l, c)