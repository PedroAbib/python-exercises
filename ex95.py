# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

geral = []
dados_jogador = {}
gols_por_partida = []

while True:
    dados_jogador['Jogador'] = str(input("Jogador: "))
    quant_partidas = int(input("Quantas partidas: "))
    total = 0
    for i in range(0, quant_partidas):
        gols = int(input(f"Quantos gols na partida {i}? "))
        total += gols
        gols_por_partida.append(gols)
    dados_jogador['Gols'] = gols_por_partida[:]
    dados_jogador['Total'] = total
    gols_por_partida.clear()
    geral.append(dados_jogador.copy())
    dados_jogador.clear()
    continuar = str(input("Deseja continuar[S / N]? ")).upper()
    if "N" in continuar:
        break

for i in range(0, len(geral)):
    print(f"=Dados do jogador {geral[i]['Jogador']}======")
    print(f"Total de partidas: {len(geral[i]['Gols'])}")
    for printa_gols in range(0, len(geral[i]['Gols'])):
        print(f"Gols na partida {printa_gols}: {geral[i]['Gols'][printa_gols]}")
    print(f"Total de gols: {geral[i]['Total']}")
    print(f"=" * 29)

print(geral)