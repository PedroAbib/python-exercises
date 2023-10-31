# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
# O programa será interrompido quando o número solicitado for negativo.

n = int(input("Digite um número(negativo para parar): "))
contagem = 1

while True:
    if n >= 0:
        print(f"{n} x {contagem} = {n * contagem}")
        contagem += 1
        if contagem == 11:
            n = int(input("Digite um número(negativo para parar): "))
            contagem = 1
    else:
        break
print("Fim.")

# Uma opção é utilizar for para controlar a contagem.