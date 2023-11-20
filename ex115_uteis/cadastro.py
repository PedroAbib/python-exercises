import json
from time import sleep
from utilidadesCeV import dado

def cadastrar(nome, idade):
    try:
        with open('arquivo.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []

    pessoa = {}
    pessoa['Nome'] = nome
    pessoa['Idade'] = idade
    dados.append(pessoa)
    with open('arquivo.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)
    feedback(f'{pessoa['Nome']} foi cadastrado com sucesso.')

def listar():
    try:
        titulo('PESSOAS CADASTRADAS')
        with open('arquivo.json', 'r') as arquivo:
            dados = json.load(arquivo)
            for i in range(0, len(dados)):
                print(f'{i + 1} - {dados[i]['Nome']:<35}{dados[i]['Idade']} anos')
    except FileNotFoundError:
        feedback('O arquivo ainda não existe.')

def feedback(txt):
    print(txt)
    sleep(1)

# Interface
def linha(tam):
    print('-' * tam)

def titulo(txt):
    tam = 50
    linha(tam)
    print(f'{txt:^{tam}}')
    linha(tam)

def menu(lista):
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    linha(50)
    opcao = dado.leiaInt('Sua Opção: ')
    return opcao