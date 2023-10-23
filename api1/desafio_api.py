from flask import Flask, jsonify, request

app = Flask(__name__)

cancoes = [
    {
        'canção': 'Quando o sol',
        'estilo': 'Rock'
    },
    {
        'canção': 'Indios',
        'estilo': 'Rock'
    },
    {
        'canção': 'Que país é este?',
        'estilo': 'Rock'
    },
]
# Rota padrão - GET https://localhost:5000
@app.route('/cancoes')
def obter_todas_cancoes():
    return jsonify(cancoes)



# Obter postagem por id - GET http://localhost:5000/cancoes
@app.route('/cancoes/<int:cancao_id>', methods=['GET'])
def obter_cancao_por_id(cancao_id):
    return jsonify(cancoes[cancao_id])

# Criar uma nova canção - POST http://localhost:5000/cancoes
@app.route('/cancoes',methods=['POST'])
def nova_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)
    return jsonify(f' A canção: {cancao} adicionada com sucesso', 200)

# Alterar uma canção existente - PUT http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:cancao_id>',methods=['PUT'])
def atualizar_cancao(cancao_id):
    cancao_alterada = request.get_json()
    cancoes[cancao_id].update(cancao_alterada)
    return jsonify(cancoes[cancao_id], 200)

# Excluir uma cancao - DELETE - http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:cancao_id>',methods=['DELETE'])
def excluir_cancao(cancao_id):
    try:
        del cancoes[cancao_id]
        return jsonify({'mensagem': 'A canção foi removida com sucesso!'})
    except:
        return jsonify('Não foi encontrado uma canção com este id', 404)
    
app.run(port=5000,host='localhost',debug=True)