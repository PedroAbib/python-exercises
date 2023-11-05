# Crie um programa que gerencie o aproveitamento de um jogador de Futebol. O programa vai ler o nome do jogador e quantas partidas
# ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

dados = {}
gols = []
total = 0

dados['Jogador'] = str(input("Jogador: "))
quant_partidas = int(input("Quantidade de partidas: "))

for p in range(0, quant_partidas):
    pergunta_gols = int(input(f"Quantos gols na partida {p}: "))
    gols.append(pergunta_gols)
    total += pergunta_gols
dados['Gols'] = gols
dados['Total'] = total
print(dados)

print(f"O jogador {dados['Jogador']} jogou {quant_partidas} partidas.")
for p in range(0, len(gols)):
    print(f"-Na partida {p}, fez {gols[p]} gols.")
print(f"Foi um total de {total} gols.")