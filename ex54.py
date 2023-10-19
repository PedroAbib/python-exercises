# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
# Considerando maioridade como 21 anos
from datetime import date

maiores = 0
menores = 0
atual = date.today().year

for idades in range(1, 7 +1):
    nascimento = int(input("Ano de nascimento: "))
    nascimento = atual - nascimento
    if nascimento < 21:
        menores += 1
    else:
        maiores += 1

print(f"Há {maiores} pessoas de maiores e {menores} menores de idade nesta lista.")