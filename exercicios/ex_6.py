
import requests


URL = 'http://localhost:5000/soma'

PAYLOAD = {
    'numeros': [
        1, 2, 3, 4, 5, 6, 7, 8, 9
    ]
}

res = requests.post(URL, json=PAYLOAD)

if res.status_code == 200:
    print('Soma = {}'.format(
        res.json().get('soma')
    ))
else:
    print(res.text)