# Faça um programa que checa os tipos de valores

n = input("Digite algo: ")
print("É alfanumérico? {} \nÉ alfabético? {} \nÉ numérico? {} \nEstá em maiúsculo? {}".format(n.isalnum(), n.isalpha(), n.isnumeric(), n.isupper()))

