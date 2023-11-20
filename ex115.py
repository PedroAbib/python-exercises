# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from ex115_uteis import cadastro
from utilidadesCeV import dado

while True:
    cadastro.titulo('MENU PRINCIPAL')
    comando = cadastro.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if comando == 1:
        cadastro.listar()
    elif comando == 2:
        nome = str(input('Nome: '))
        idade = dado.leiaInt('Idade: ')
        cadastro.cadastrar(nome, idade)
    elif comando == 3:
        cadastro.feedback('Finalizando o programa...')
        break
    else:
        cadastro.feedback('Erro, digite uma opção válida.')