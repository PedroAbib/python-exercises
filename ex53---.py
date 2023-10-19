# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: "Apos a sopa", "A sacada da casa", "A torre da derrota"

frase = input("Digite uma frase: ").replace(" ", "").upper()

frase_invertida = ""
# Este for cria a versão invertida de frase!
for letra in frase:
    frase_invertida = letra + frase_invertida

frase_invertida = frase_invertida.replace(" ", "").upper()

if frase in frase_invertida:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")

print(f"Frase formatada ({frase}), frase invertida ({frase_invertida})")