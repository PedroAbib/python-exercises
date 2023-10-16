# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input("Ângulo: "))

print("O seno de {} é {}, cosseno é {}, e a tangente é {}".format(angulo, math.sin(angulo), math.cos(angulo), math.tan(angulo)))

