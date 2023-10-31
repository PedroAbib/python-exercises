# Crie uma Tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação
# Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time da Corinthians.

tabela = ('Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Flamengo', 'Atlético-MG', 'Athletico-PR', 'Fluminense', 'Fortaleza', 'Cuiabá', 'São Paulo', 'Internacional', 'Cruzeiro', 'Corinthians', 'Bahia', 'Santos', 'Goiás', 'Vasco', 'Coritiba', 'América-MG')

print(f"Os 5 primeiros colocados são: {tabela[:5]}")
print(f"Os 4 últimos colocados são: {tabela[16:]}")
print(f"Em ordem alfabética: {sorted(tabela)}")
print(f"Corinthians está na posição {tabela.index('Corinthians') + 1}")
