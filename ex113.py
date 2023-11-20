# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from utilidadesCeV import dado

numero = dado.leiaInt('Digite um número inteiro: ')

print(numero)

real = dado.leiaFloat('Digite um número real: ')

print(real)