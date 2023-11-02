# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

dados = []
aluno = []
espacamento = " " * 14

while True:
    aluno.append(input("Nome: "))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    dados.append(aluno[:])
    aluno.clear()
    continuar = input("Deseja continuar [S / N]? ").upper().strip()
    if "N" in continuar:
        break
print(dados)
print("="*40)
print(f"No.{espacamento}NOME{espacamento}MÉDIA")
for alunos in range(0, len(dados)):
    print(f"{alunos}{dados[alunos][0]:^35}{(dados[alunos][1] + dados[alunos][2]) / 2:.1f}")
print("="*40)

while True:
    notas = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if notas == 999:
        break
    else:
        if notas < len(dados) and notas >= 0:
            print(f"Notas de {dados[notas][0]} são: {dados[notas][1:]}")
        else:
            print("Opção inválida, tente novamente.")
print("Finalizando.")

# Ao invés de criar um lista separada, posso criar um input direto que já insere uma nova lista dentro de outra
# Ex.   item = input()
#       item1 = input()
#       item2 = input()
#       lista.append([item, item1, item2])