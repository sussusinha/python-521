
class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.cartao_de_credito = None
        
    def to_json(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    def verify_password(self, password):
        return self.password == password

class CartaoDeCredito:
    
    def __init__(self, banco):
        self.banco = banco

class Veiculo:
    pass

class Banco:
    pass

if __name__ == "__main__":
    
    # Momento do cadastro
    lucas = User('Lucas', 'lucas@email.com', 'admin')

    # Momento do login
    if lucas.verify_password('admin'):
        print('Senha correta')
    else:
        print('Senha incorreta')

    if lucas.password == password:
