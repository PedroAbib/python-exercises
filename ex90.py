# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.

dados = {}

dados['Nome'] = str(input("Nome: "))
dados['Média'] = float(input("Média: "))

if dados['Média'] < 6:
    dados['Situacão'] = "Reprovado"
else:
    dados['Situação'] = "Aprovado"

for n, c in dados.items():
    print(f"{n}: {c}")