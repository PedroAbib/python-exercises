# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

lista = [[[],[],[]],
         [[],[],[]],
         [[],[],[]]]

soma_pares = 0
soma_coluna3 = 0
maior_valor_linha2 = None

for posicao in range(0, len(lista)):
    for indice in range(0, len(lista[posicao])):
        lista[posicao][indice].append(int(input(f"Digite um número para a posição[{posicao}, {indice}]: ")))
        if lista[posicao][indice][0] % 2 == 0:
            soma_pares += lista[posicao][indice][0]
        if indice == 2:
            soma_coluna3 += lista[posicao][indice][0]
print(f"{lista[0]} \n{lista[1]} \n{lista[2]}")
print(f"A soma de todos os números pares resulta em {soma_pares}.")
print(f"A soma dos números na coluna 3 resulta em {soma_coluna3}.")
print(f"O maior valor da 2ª linha é {sorted(lista[1])[2]}")