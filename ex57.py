# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado,
# peça a digitação novamente até ter um valor correto.
r = ""

while r != "M" and r != "F":
    r = input("Sexo [M/F]: ").upper()
    if r != "M" and r != "F":
        print("Informe [M] ou [F].")
print("Fim.")