# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

largura = int(input("Largura: "))
altura = int(input("Altura: "))

print("Área: {} \nQuantidade de tinta: {}".format(largura * altura, (largura * altura) / 2))