
import requests


URL = 'https://gen-net.herokuapp.com/api/users'

def encontrar_usuario(email):
    res = requests.get(URL, params={
        'email': email
    })
    if res.status_code == 200:
        r = res.json()
        return r[0] if len(r) > 0 else None
    return None

def atualizar_senha(usuario, nova_senha):
    requests.put(URL + '/' + str(usuario.get('id')), data={
        'password': nova_senha
    })

email = input('Digite seu email: ')

usuario = encontrar_usuario(email)

if not usuario:
    print('Usuário não encontrado')
else:
    nova_senha = input('Digite sua nova senha: ')
    atualizar_senha(usuario, nova_senha)
    print('Senha atualizada com sucesso')
