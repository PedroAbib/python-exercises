# Crie um programa que tenha uma Tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Caderno', 15.90, 'Livro', 34.5, 'Mochila', 96, 'Estojo', 13.5, 'Caneta', 5)
titulo = 'LISTAGEM DE PREÇOS'

print(f"{titulo:=^47}")
for produto in range(0, len(listagem), 2):
    print(f"{listagem[produto]:.<40}R${listagem[produto + 1]:.2f}")
print("="*47)