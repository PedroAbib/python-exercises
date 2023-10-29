# Melhore o jogo do Desagio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

jogador = None
computador = randint(0, 10)
palpites = 0

while computador != jogador:
    jogador = int(input("Adivinhe um número inteiro de 0 a 10: "))
    palpites += 1
    if computador != jogador:
        print("Tente novamente.")

print(f"Após {palpites} palpites, você acertou, o número escolhido pelo computador foi {computador}")
