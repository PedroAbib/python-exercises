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