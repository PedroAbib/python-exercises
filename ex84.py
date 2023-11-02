# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
pesados = []
leves = []
maior_peso = menor_peso = 0
while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))
    if maior_peso == 0:
        maior_peso = dados[1]
        menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        elif dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = input("Deseja continuar[S / N]? ").upper().strip()
    if "N" in continuar:
        break

for p in range(0, len(pessoas)):
        if pessoas[p][1] == maior_peso:
            pesados.append(pessoas[p][0])
        elif pessoas[p][1] == menor_peso:
             leves.append(pessoas[p][0])

print("="*20)
print(f"Total de cadastros: {len(pessoas)}")
print(f"O maior peso foi {maior_peso}Kg. Peso de {pesados}.")
print(f"O menor peso foi {menor_peso}Kg. Peso de {leves}.")