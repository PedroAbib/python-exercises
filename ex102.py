# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro
# chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    global numero
    for i in range(numero - 1, 0, -1):
        n *= i
    if show == True:
        print(f"{numero}! = {numero}", end="")
        for i in range(numero - 1, 0, -1):
            print(f"x{i}", end="")
        print(f" = {n}")
    return n

numero = int(input("Digite um número: "))
conta = input("Deseja visualizar a conta[S / N]? ").upper()
if "S" in conta:
    conta = True

print(f"O fatorial de {numero} é igual a {fatorial(numero, conta)}")
