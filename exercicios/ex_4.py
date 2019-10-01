
import requests


URL = 'https://gen-net.herokuapp.com/api/users'

payload = {
    'name': input('Digite seu nome: '),
    'email': input('Digite seu email: '),
    'password': input('Digite sua senha: ')
}

response = requests.post(URL, data=payload)

if response.status_code == 200:
    print(response.json())
else:
    print(response.text)
