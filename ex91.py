# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

dados = {}

for rola_dado in range(1, 5):
    dados[f'Jogador{[rola_dado]}'] = randint(1, 6)

print("=JOGADAS" + ("=" * 10))
for j, r in dados.items():
    print(f"{j} rolou {r}")
    sleep(0.5)
print("=" * 18)

print("=PLACAR" + ("=" * 11))
placar = dict(sorted(dados.items(), key=lambda x:x[1], reverse=True))
colocacao = 1
for p, u in placar.items():
    print(f"{colocacao}º: {p} com {u}")
    colocacao += 1
print("=" * 18)
