# Melhore o Desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar 0 termos.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))
iteracao = 10

print(f"({termo}", end="")
while iteracao > 1:
    termo += razao
    print(f", {termo}", end="")
    iteracao -= 1
    if iteracao == 1:
        print(")")
        continua = int(input("Quantos termos quer adicionar? "))
        iteracao += continua
print("Fim.")