# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu [preço normal] e [condição de pagamento]:
# -à vista dinheiro/cheque: 10% de desconto
# -à vista no cartão: 5% de desconto
# -em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros

produto = float(input("Valor do produto: R$"))

pagamento = int(input("Opção de pagamento: \n1 - à vista dinheiro/cheque \n2 - à vista no cartão \n3 - 2x no cartão \n4 - 3x ou mais no cartão \nDigite a opção: "))

avista_dinheiro = produto - (produto * 10/100)

avista_cartao = produto - (produto * 5/100)

cartao_3xmais = produto + (produto * 20/100)

if pagamento == 1:
    print("O produto no valor de R${:.2f} terá um desconto de 10%, valendo R${:.2f}".format(produto, avista_dinheiro))

elif pagamento == 2:
    print("O produto no valor de R${:.2f} terá um desconto de 5%, valendo R${:.2f}".format(produto, avista_cartao))

elif pagamento == 3:
    print("O produto vale R${:.2f}".format(produto))

elif pagamento == 4:
    print("O produto no valor de R${:.2f} sofrerá juros de 20%, valendo R${:.2f}".format(produto, cartao_3xmais))

else:
    print("O número não corresponde a uma das opções.")