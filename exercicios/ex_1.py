
import requests


cep = input('Digite seu cep: ')

URL = 'https://viacep.com.br/ws/{}/json/'.format(cep)

response = requests.get(URL)

if response.status_code == 200:
    logradouro = response.json().get('logradouro')
    print(logradouro)
else:
    print(response.text)

