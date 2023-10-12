# Receba 3 inputs de um usuário
# Cada input representa um lado de um triângulo
# Verifique a condição de existência de um triangulo
# Se o triangulo existir, print os seus 3 lados e "Triângulo válido."
# Se o triangulo não existir, print "Triângulo impossível."

def verifica_lado_verdadeiro(target, test1, test2):
    soma = test1 + test2
    subtracao = abs(test1 - test2)
    return target > subtracao and target < soma

print("Digite os lados do triângulo: ")

lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

lado1_verdadeiro = verifica_lado_verdadeiro(lado1, lado2, lado3)
lado2_verdadeiro = verifica_lado_verdadeiro(lado2, lado1, lado3)
lado3_verdadeiro = verifica_lado_verdadeiro(lado3, lado1, lado2)

if lado1_verdadeiro and lado2_verdadeiro and lado3_verdadeiro:
    print(f"Lado 1: {lado1}")
    print(f"Lado 2: {lado2}")
    print(f"Lado 3: {lado3}")
    print("Triângulo verdadeiro.")

else:
    print("Triângulo impossível.")