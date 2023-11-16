# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols
# ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
    if nome == "" or nome.isnumeric():
        nome = "<desconhecido>"
    if gols == "" or gols.isnumeric() == False:
        gols = 0
    print(f"O jogador {nome} marcou {gols} gols.")

jogador = (input("Nome do Jogador: ")).strip()
marcou = (input("Quantos gols marcou: ")).strip()

ficha(jogador, marcou)