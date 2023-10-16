# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza
#      primeiro = Ana
#      último = Souza

nome_completo = input("Nome Completo: ").strip()

nome_splitado = nome_completo.split()

print("Primeiro Nome: {}".format(nome_splitado[0]))

print("Último Nome: {}".format(nome_splitado[-1]))