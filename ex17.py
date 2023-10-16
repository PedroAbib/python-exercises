# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre
# o comprimento da hipotenusa
import math

cateto_oposto = float(input("Cateto Oposto: "))
cateto_adjacente = float(input("Cateto Adjacente: "))

hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)

print("A hipotenusa é: {:.2f}".format(hipotenusa))