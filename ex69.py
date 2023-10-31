# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# que ou não continuar. No final, mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

mais_18 = homens = mulheres_sub20 = 0

while True:
    idade = int(input("Idade: "))
    if idade > 18:
        mais_18 += 1
    sexo = input("Selecione o sexo[M / F]: ").upper().strip()
    if "F" in sexo and idade < 20:
        mulheres_sub20 += 1
    elif "M" in sexo:
         homens += 1
    continuar = input("Deseja continuar[S / N]? ").upper().strip()
    if "N" in continuar:
        break
print(f"Maior de 18 anos: {mais_18} \nHomens cadastrados: {homens} \nMulheres menores de 20 anos: {mulheres_sub20}")