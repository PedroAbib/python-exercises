def leiaDinheiro(prompt=''):
    while True:
        print(prompt, end="")
        num = input()
        if num.isnumeric() or num.replace('.', '', 1).isnumeric() or num.replace(',', '', 1).isnumeric():
            num = float(num.replace(',', '.'))
            break
        else:
            print('Erro, digite um valor numérico para o preço.')
    return num

def leiaInt(prompt=''):
    while True:
        try:
            print(prompt, end="")
            num = int(input())
        except (ValueError, TypeError):
            print("Erro, digite um número inteiro.")
        else:
            return num
        

def leiaFloat(prompt=''):
    while True:
        try:
            print(prompt, end='')
            num = float(input())
        except (ValueError, TypeError):
            print('Valor de tipo não númerico(real), tente novamente.')
        else:
            return num