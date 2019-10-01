
import flask


app = flask.Flask(__name__)

@app.errorhandler(404)
def handle_404(error):
    return '#LULAPRESO'

@app.route('/hello-world')
def get_hello_world():
    return 'hello, world'

@app.route('/soma', methods=[ 'POST' ])
def soma():

    numeros = flask.request.json.get('numeros')
    
    if not numeros:
        return 'Chave "numeros" não encontrada', 400

    if type(numeros) is not list:
        return '"numeros" deve ser uma lista', 400

    return flask.jsonify({
        'soma': sum(numeros)
    })

@app.route('/users', methods=[ 'GET' ])
def get_users():
    return 'get users'

@app.route('/users', methods=[ 'POST' ])
def create_user():
    return 'create user'

if __name__ == '__main__':
    app.run(debug=True)