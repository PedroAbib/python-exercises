# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
# dessa progressão.

primeiro_termo = int(input("Determine o primeiro termo: "))
razao = int(input("Determine a razão da PA: "))

for pa in range(primeiro_termo, (primeiro_termo + (10 - 1) * razao) + 1, razao):
    print(f"({pa})")

# Para limitar o for até o 10º termo, utilizei a fórmula do termo geral da PA, somei +1 ao final para incluir o 10º termo no print