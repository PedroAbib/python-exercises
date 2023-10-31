# Crie um menu que receba um input do usuário
# Recebe um número de 1 a 5
# Se o valor for diferente disto, print "Erro, valor inválido"
# Opção 1: Registrar uma nova transferência
# Opção 2: Mostrar todas as transferência
# Opção 3: Editar uma transferência
# Opção 4: Remover uma transferência
# Opção 5: Parar
# Registrar uma transferência: pegue do usuário um nome, um valor e uma descrição, tudo na mesma linha separado por traços
# Após pegar os valores, a transferência tem que ter um ID numérico de 5 números aleatórios. O ID deve ser único
# Mostrar todas as transferencias: Após escolher essa opção, perguntar se o usuario quer de forma ascendente ou descendente
# Editar: Peça o ID de uma transferencia e o novo preço na mesma linha, se o usuario fornecer um ID invalido print "ID invalido" e volte para o menu
# Remover: Peça o ID de uma transferencia, print o elemento e pergunte se o usuario confirma, se sim delete, se não volte para o menu, se o usuario fornecer um ID invalido print "ID invalido" e volte para o menu

from random import randint

transferencias = {}

while True:
    operacao = (input("-Menu- \n[1] Registrar uma nova transferência \n[2] Mostrar todas as transferência \n[3] Editar uma transferência \n[4] Remover uma transferência \n[5] Parar \nEscolha a operação:"))

    if operacao == "1":
        registrar = input("Digite um nome para a transferência, o valor e a descrição(separado por traços): ").split('-')
        registrar[1] = float(registrar[1])
        while True:
            novo_id = str(randint(10000, 99999))
            if novo_id not in transferencias:
                transferencias[novo_id] = registrar
                break

    elif operacao == "2":
        ordem = input("[1] Ascendente \n[2] Descendente \nEm que ordem deseja visualizar? ")
        if ordem == "1":
            transferencias_asc = sorted(transferencias.items(), key=lambda x: x[1][1])
            for id, transferencia in transferencias_asc:
                print(f"{id}, {transferencia}")
        elif ordem == "2":
            transferencias_desc = sorted(transferencias.items(), key=lambda x: x[1][1], reverse=True)
            for id, transferencia in transferencias_desc:
                print(f"{id}, {transferencia}")
        else:
            print("Opção inválida.")

    elif operacao == "3":
        editar = input("Digite o ID da transferência e o novo preço(separado por traços): ").split('-')
        if editar[0] in transferencias:
            transferencias[editar[0]][1] = editar[1]
        else:
            print("ID inválido.")

    elif operacao == "4":
        remover = input("Digite o ID da transferência que deseja remover: ")
        if remover in transferencias:
            print(transferencias[remover])
            confirmar = input("Tem certeza que deseja remover esta transferência[S/N]? ").upper()
            if "S" in confirmar:
                del transferencias[remover]
        else:
            print("ID inválido.")

    elif operacao == "5":
        break

    else:
        print("Erro, valor inválido.")
