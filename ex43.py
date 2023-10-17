# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"O IMC:{imc} representa abaixo do peso.")

elif imc > 18.5 and imc < 25:
    print(f"O IMC:{imc} representa peso ideal.")

elif imc >= 25 and imc < 30:
    print(f"O IMC:{imc} representa sobrepeso.")

elif imc >= 30 and imc < 40:
    print(f"O IMC:{imc} representa obesidade.")

else:
    print(f"O IMC:{imc} representa obesidade mórbida")