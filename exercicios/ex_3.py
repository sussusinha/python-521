
import requests


email = input('Digite seu email: ')

URL = 'https://gen-net.herokuapp.com/api/users'

response = requests.get(URL, params={
    'email': email
})

if response.status_code == 200:
    print(response.json())
else:
    print(response.text)