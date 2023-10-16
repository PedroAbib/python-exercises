# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R#0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

distancia = int(input("Distância em Km: "))

viagem_ate_200 = 0.5 * distancia

viagem_longa = 0.45 * distancia

if distancia <= 200:
    print("Preço: R${:.2f}".format(viagem_ate_200))

else:
    print("Preço: R${:.2f}".format(viagem_longa))