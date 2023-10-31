# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

vitorias = 0

while True:
    numero = int(input("Digite um número positivo: "))
    if numero >= 0:
        jogada = input("Par ou Ímpar [P / I]?" ).upper()
        if "P" or "I" in jogada:
            computador_numero = randint(0, 10)
            total = numero + computador_numero
            print(f"Você escolheu {numero} e o computador {computador_numero}. O total é {total}.")
            print("Resultado PAR" if total % 2 == 0 else "Resultado ÍMPAR")
            if total % 2 == 0 and "P" in jogada or total % 2 != 0 and "I" in jogada:
                print("Você venceu.")
                vitorias += 1
            else:
                print("Você perdeu.")
                break
        else:
            print("Opção inválida.")
print(f"Winstreak: {vitorias}")