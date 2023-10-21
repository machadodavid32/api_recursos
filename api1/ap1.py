from flask import Flask, jsonify, request

# Iremos criar uma api de blog onde iremos editar, criar e excluir postagens em um blog usando api


app = Flask(__name__)
postagens = [
    {
        'titulo': 'Minha História',
        'autor': 'Amanda Dias'
         
                },
    {
        
        'titulo': 'Novo Dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    {
        'titulo': 'Lnaçamento do Ano',
        'autor': 'Jeff Bezos'
    }
]
# Definir rota padrão - GET http://localhost:5000/
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

@app.route('/postagens', methods=['GET'])
def obter_postagem_por_id(indice):
    return jsonify(postagens[indice], 200)

app.run(port=5000, host='localhost', debug=True)