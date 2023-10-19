# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# -A média de idade do grupo.
# -Qual é o nome do homem mais velho.
# -Quantas mulheres têm menos de 20 anos.
nome = None
idade = None
sexo = None

soma_idade = 0
mulheres_20 = 0

homem_velho = 0
nome_homem = None

for teste in range(1, 5):
    nome = input(f"Nome {teste}: ")
    idade = int(input(f"Idade {teste}: "))
    sexo = input(f"Sexo {teste}: ")
    soma_idade += idade
    if "feminino" in sexo and idade < 20:
        mulheres_20 += 1
    if "masculino" in sexo and idade > homem_velho:
        nome_homem = nome
        homem_velho = idade

media_idade = soma_idade / 4

print(f"A média de idade do grupo é: {media_idade}")
print(f"O homem mais velho se chama {nome_homem}")
print(f"Há {mulheres_20} mulheres com menos de 20 anos no grupo.")