# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo
# a validação para aceitar apenas um valor numérico.
# Ex.: n = leiaInt('Digite um n')

def leiaInt(prompt=''):
    while True:
        print(prompt, end="")
        num = input()
        if num.isnumeric():
            print("Valor numérico aceito.")
            break
        else:
            print("Valor não numérico, tente novamente.")


n = leiaInt('Digite um número: ')

