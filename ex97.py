# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.
# Ex: escreva('Olá, Mundo!')
# Saída: ~~~~~~~~~~~~~
#         Olá, Mundo!
#        ~~~~~~~~~~~~~

def escreva(txt):
    linha = "=" * (len(txt) + 2)
    print(linha)
    print(f"{txt:^{len(linha)}}")
    print(linha)

escreva(input("Escreva algo: "))