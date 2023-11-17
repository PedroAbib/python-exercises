def aumentar(valor, aumento, form=False):
    valor += (aumento / 100) * valor
    if form:
        return moeda(valor)
    else:     
        return valor


def diminuir(valor, diminui, form=False):
    valor -= (diminui / 100) * valor
    if form:
        return moeda(valor)
    else:     
        return valor


def dobro(valor, form=False):
    valor *= 2
    if form:
        return moeda(valor)
    else:     
        return valor


def metade(valor, form=False):
    valor /= 2
    if form:
        return moeda(valor)
    else:     
        return valor


def moeda(valor):
    return f'R${valor:.2f}'


def resumo(valor, aument, dimin):
    titulo = 'RESUMO DO VALOR'
    tam = 30
    print('-' * tam)
    print(f'{titulo:^{tam}}')
    print('-' * tam)
    print(f'Preço analisado:  {moeda(valor)}')
    print(f'Dobro do preço:   {moeda(dobro(valor))}')
    print(f'Metade do preço:  {moeda(metade(valor))}')
    print(f'{aument}% de aumento:   {moeda(aumentar(valor, aument))}')
    print(f'{dimin}% de redução:   {moeda(diminuir(valor, dimin))}')
    print('-' * tam)
