# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_pares = []
lista_impares = []

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    continua = input("Deseja continuar[S / N]? ").upper().strip()
    if "N" in continua:
        break
print(f"Lista original: {lista}")

for p in lista:
    if p % 2 == 0:
        lista_pares.append(p)
print(f"Lista de pares: {lista_pares}")

for i in lista:
    if i % 2 != 0:
        lista_impares.append(i)
print(f"Lista de Ímpares: {lista_impares}")

# Uma opção é aninhar um dos for ao outro, utilizando um for com enumerate e adicionar os termos a cada lista