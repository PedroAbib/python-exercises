# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import requests

url = 'http://www.pudim.com.br/'

try:
    response = requests.get(url)
except:
    print('Não foi possível acessar o site Pudim.')
else:
    print('É possível acessar o site Pudim.')