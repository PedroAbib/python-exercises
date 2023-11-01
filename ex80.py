# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for contagem in range(0, 5):
    num = int(input("Digite um número: "))
    if contagem == 0:
        lista.append(num)
        print(f"Numero adicionado ao início da lista. Na posição {lista.index(num)}")
    else:
        if num <= lista[0]:
            lista.insert(0,num)
            print(f"Número adicionado ao início da lista. Na posição {lista.index(num)}")
        elif num >= lista[-1]:
            lista.append(num)
            print(f"Número adicionado ao final da lista. Na posição {lista.index(num)}")
        else:
            if num <= lista[1]:
                lista.insert(1, num)
                print(f"Número adicionado a lista. Na posição {lista.index(num)}")
            elif num <= lista[2]:
                lista.insert(2, num)
                print(f"Número adicionado a lista. Na posição {lista.index(num)}")
            elif num <= lista[3]:
                lista.insert(3, num)
                print(f"Número adicionado a lista. Na posição {lista.index(num)}")
            elif num <= lista[4]:
                lista.insert(4, num)
                print(f"Número adicionado a lista. Na posição {lista.index(num)}")
print(lista)

# Uma opção é usar while para checar cada posição do início ao fim e inserindo quando for válido.