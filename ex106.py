# Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando
# o usuário digitar a palavra 'Fim', o programa se encerrará.
# OBS: use cores.
from time import sleep

def titulo(txt):
    print('=' * (len(txt) + 4))
    print(f'  {txt}')
    print('=' * (len(txt) + 4))

while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    target = str(input("Função ou Biblioteca ['fim' para finalizar] > ")).strip().lower()
    if target == 'fim':
        break
    else:
        titulo(f'Acessando o manual do comando {target}')
        sleep(0.5)
        print(help(target))
        sleep(0.5)