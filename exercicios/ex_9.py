
x = [ 0, 1, 2 ]
y = { 'nome': 'Lucas' }

def operacao():
    # x[5]            # erro de lista
    # y['dasda']        # erro de dicionário   
    5 / 0             # erro de divisão por zero

operacao()

try:
    operacao()
except IndexError:
    print('Erro de lista')
except KeyError:
    print('Erro de dicionário')
except ZeroDivisionError:
    print('Erro de divisão por zero')
except Exception:
    print('Erro genérico')