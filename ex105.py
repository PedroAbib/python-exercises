# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes
# informações:
# -Quantidade de notas
# -A maior nota
# -A menor nota
# -A média da turma
# -A situação (opcional)
# Adicione também as docstrings da função.

def notas(* notas, sit=False):
    """
    Função que analisa uma quantidade qualquer de notas.

    Parâmetros:
    -notas: adicione as notas a serem analisadas, separadas por vírgula.
    -sit: adicione 'sit=True' para que a função retorne também a situação.

    Retorna:
    Dicionário com: a quantidade de notas fornecidas, a maior e menor nota, a média, e opcionalmente, a situação.
    """
    dados = {}
    maior = notas[0]
    menor = notas[0]
    soma_media = 0
    dados['Quantidade de Notas'] = len(notas)
    for i in notas:
        soma_media += i
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
    dados['Maior nota'] = maior
    dados['Menor nota'] = menor
    dados['Média da Turma'] = soma_media / len(notas)
    if sit:
        if dados['Média da Turma'] >= 7:
            dados['Situação'] = 'Aprovado'
        else:
            dados['Situação'] = 'Reprovado'
    print(dados)
    return dados

notas(3.5,7,6.3,5, sit=True)