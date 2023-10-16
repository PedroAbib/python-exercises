# Faça um programa que leia uma frase pelo teclado e mostre:
# -Quantas vezes aparece a letra "A"
# -Em que posição ela aparece a primeira vez
# -Em que posição ela aparece a última vez

frase = input("Digite uma frase: ").strip()

primeiro_a = frase.lower().find('a') + 1

ultimo_a = frase.lower().rfind('a') + 1

print("Quantidade de letra 'a' na frase: {}".format(frase.lower().count('a')))

print("Posição da primeira letra 'a': {}".format(primeiro_a))

print("Posição da última letra 'a': {}".format(ultimo_a))