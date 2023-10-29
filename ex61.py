# Regaça o Desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão para a PA: "))
iteracao = 10

print(f"({termo}", end="")
while iteracao > 1:
    termo += razao
    print(f", {termo}", end="")
    iteracao -= 1
print(")")