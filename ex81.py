# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

lista = []
quantidade = 0

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    quantidade += 1
    continua = input("Deseja continuar[S / N]? ").upper().strip()
    if "N" in continua:
        break
lista_decrescente = sorted(lista, reverse=True)
print(f"Um total de {quantidade} números foram digitados.")
print(f"A lista ordenada de forma decrescente: {lista_decrescente}")
if 5 in lista:
    print("Existe o valor 5 na lista.")
else:
    print("Não existe o valor 5 na lista.")

# Em vez de criar uma variável quantidade, uma opção é mostrar a len(lista)