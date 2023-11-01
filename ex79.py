# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []

while True:
    n = int(input("Digite um valor numérico: "))
    if n not in valores:
        valores.append(n)
        print("Valor adicionado.")
    else:
        print("Número já existe.")
    continuar = input("Deseja continuar[S / N]? ").upper().strip()
    if "N" in continuar:
        break
print(sorted(valores))