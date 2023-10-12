# Pegar input do usuário que representa sua idade
# Verificar a idade do usuário, e se ela for maior que 65, print "Pode se aposentar."
# Se for menor que 18, print "Pode estudar."
# Se for entre 18 e 65 anos, print "Precisa trabalhar."
# Se o valor for menor que 0, print "Erro."
# Desconsiderar valores acima de 100, print "Erro."

idade_usuário = int(input("Qual a sua idade? "))

if idade_usuário < 0 or idade_usuário > 100:
    print("Erro.")

else:

    if idade_usuário > 65:
        print("Pode se aposentar.")

    elif idade_usuário < 18:
        print("Precisa estudar.")

    else:
        print("Precisa trabalhar.")



