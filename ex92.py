# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar(Considerar 35 anos de contribuição).
from datetime import date

dados = {}

dados['Nome'] = str(input("Nome: "))
ano_nascimento = int(input("Ano de Nascimento: "))
dados['Idade'] = date.today().year - ano_nascimento
dados['CTPS'] = int(input("Carteira de Trabalho (0 se não tiver): "))
if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input("Ano de Contratação: "))
    dados['Salário'] = float(input("Salário: R$"))
    dados['Aposentadoria'] = dados['Idade'] + (35 - (date.today().year - dados['Ano de Contratação']))
else:
    dados['CTPS'] = 'Não possui.'

for chave, valor in dados.items():
    print(f"{chave}: {valor}")