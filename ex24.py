# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input("Cidade: ")

cidade_split = cidade.lower().split()

print("O nome começa com 'Santo'? {}".format('santo' in cidade_split[0]))