contador = 0

for c in range(0, 1000001):
    print(c)
    contador += 1
    for d in range(0, 1000001):
        print(d)
        contador += 1
        for e in range(0, 1000001):
            print(e)
            contador += 1
print(contador)