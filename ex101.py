# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando
# um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f"Com {idade} anos: ", end="")
    if idade >= 18 and idade < 70:
        print("Voto OBRIGATÓRIO")
    elif idade >= 16 or idade >= 70:
        print("Voto OPCIONAL")
    else:
        print("Voto NEGADO")

voto(int(input("Ano de nascimento: ")))