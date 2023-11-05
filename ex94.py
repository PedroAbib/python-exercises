# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo.
# c) Uma lista com todas as mulheres.
# d) Uma lista com todas as pessoas com idade acima da média.

lista = []
dados = {}
total_idade = 0

while True:
    dados['Nome'] = str(input("Nome: "))
    dados['Sexo'] = str(input("Sexo[M / F]: ")).upper()
    dados['Idade'] = int(input("Idade: "))
    lista.append(dados.copy())
    total_idade += dados["Idade"]
    dados.clear()
    continuar = str(input("Deseja continuar[S / N]?" )).upper()
    if "N" in continuar:
        break
media = float(total_idade / len(lista))
print(f"Total de cadastros: {len(lista)}")
print(f"Média de idade: {media}")

print("-Lista de Mulheres---------------")
for p in lista:
    if "F" in p['Sexo']:
        print(f"-{p['Nome']}")
print("---------------------------------")

print("-Lista de idade acima da média---")
for p in lista:
    if p['Idade'] > media:
        print(f"{p['Nome']} com {p['Idade']} anos")
print("---------------------------------")