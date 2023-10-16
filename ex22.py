# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -O nome com todas as letras maiúsculas
# -O nome com todas minúsculas
# -Quantas letras ao todo(sem considerar espaços)
# -Quantas letras tem o primeiro nome.

nome = input("Nome: ")

nome_sem_espacos = nome.replace(" ", "")

primeiro_nome = nome.split()

print("Maiúsculo: {} \nMinúsculo: {}".format(nome.upper(), nome.lower()))

print("Total de letras: {} \nLetras no primeiro nome: {}".format(len(nome_sem_espacos), len(primeiro_nome[0])))