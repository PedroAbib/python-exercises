# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custa R$7,00 por cada Km acima do limite.

velocidade = int(input("Velocidade: "))

multa_por_km = 7
multa = multa_por_km * (velocidade - 80)

if velocidade > 80:
    
    print("Multa de R${:.2f}.".format(multa))