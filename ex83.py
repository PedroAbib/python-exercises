# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados na ordem correta.

expressao = input("Digite a expressão: ")
valido = False

if "(" in expressao or ")" in expressao:
    if expressao.count("(") == expressao.count(")"):
        if ")" not in expressao[0] and "(" not in expressao[-1]:
            for a in range(0, len(expressao)):
                if "(" in expressao[a] and ")" in expressao[a:]:
                    valido = True

    if valido: # Como "valido" é booleano, não preciso indicar se é == True ou False
        print("Expressão válida.")
    else:
        print("Expressão inválida.")
else:
    print("Não há parênteses.")
