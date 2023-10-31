# Crie um programa que tenha uma Tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra
# Quais são as suas vogais.

tupla = ('Chatuba', 'Onomatopeia', 'Elementar', 'Magnanimo', 'Patrick', 'Edvaldo', 'Girley', 'Voldemort', 'Morango', "K'sante")

for palavras in tupla:
    print(f"\nVogais presentes em {palavras}:")
    for letras in palavras:
        if letras in "aeiouAEIOU":
            print(f"{letras} ".lower(), end="")