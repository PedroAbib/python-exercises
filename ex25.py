# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = input("Nome: ").strip().lower()

print("Tem 'Silva' no nome? {}".format('silva' in nome))