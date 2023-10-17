# Faça um programa que leia o ano de nascimento de um jovem e informe, de acodo com sua idade:
# -Se ele ainda vai se alistar ao serviço militar.
# -Se é a hora de se alistar.
# -Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input("Idade: "))

plural_anos = 18 - idade 

if idade < 18:
    print("Faltam {} anos para se alistar ao serviço militar.".format(18 - idade))

elif idade == 18:
    print("Está na hora de se alistar.")

else:
    print("Já se passaram {} anos do prazo de alistamento.".format(idade - 18))