from flask import Flask, jsonify, request
from estrutura_banco_de_dados import Autor, Postagem, app, db
 
# Rota padrão(Pode ser entendido como GET passando o URL Base http://localhost:5000)
@app.route('/')
def obter_postagens():
    postagens = Postagem.query.all()
    lista_de_postagens = []
    for postagem in postagens:
        postagem_atual = {}
        postagem_atual['id_postagem'] = postagem.id_postagem
        postagem_atual['titulo'] = postagem.titulo
        postagem_atual['email'] = postagem.email
        lista_de_postagens.append(postagem_atual)
    return jsonify({'postagens': lista_de_postagens})
 
# GET - Obter postagem por Id - GET http://localhost:5000/postagem/1
@app.route('/postagem/<int:id_postagem>', methods=['GET'])
def obter_postagem_por_indice(id_postagem):
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem:
        return jsonify('Postagem não encontrada!')
    postagem_atual = {}
    postagem_atual['id_postagem'] = postagem.id_postagem
    postagem_atual['titulo'] = postagem.titulo
    postagem_atual['email'] = postagem.email
    return jsonify({'postagem': postagem_atual})
 
# Criar uma nova postagem - POST http://localhost:5000/postagem
@app.route('/postagem', methods=['POST'])
def nova_postagem():
    nova_postagem = request.get_json()
    postagem = Postagem(titulo=nova_postagem['titulo'], senha=nova_postagem['senha'], email=nova_postagem['email'])
    db.session.add(postagem)
    db.session.commit()
    return jsonify({'mensagem':'Postagem criada com sucesso!'}, 200)
 
# Alterar uma postagem existente - PUT http://localhost:5000/postagem/indice
@app.route('/postagem/<int:id_postagem>', methods=['PUT'])
def alterar_postagem(id_postagem):
    postagem_alterada = request.get_json()
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem:
        return jsonify({'mensagem':'Esta postagem não foi encontrada.'})
    try:
        if postagem_alterada['titulo']:
            postagem.titulo = postagem_alterada['titulo']
    except:
        pass
    try:
        if postagem_alterada['email']:
            postagem.email = postagem_alterada['email']
    except:
        pass
    try:
        if postagem_alterada['senha']:
            postagem.senha = postagem_alterada['senha']
        db.session.commit()
    except:
        pass
    return jsonify({'mensagem':'Postagem alterada com sucesso!'})
 
# DELETE http://localhost:5000/cancoes/indice
@app.route('/postagem/<int:id_postagem>', methods=['DELETE'])
def deletar_postagem(id_postagem):
    postagem_existente = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem_existente:
        return jsonify({'mensagem':'Esta postagem não foi encontrada.'})
    db.session.delete(postagem_existente)
    db.session.commit()
    return jsonify({'mensagem':'Postagem excluída com sucesso!'})
   
@app.route('/autores')
def obter_autores():
    autores = Autor.query.all()
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_de_autores.append(autor_atual)
    return jsonify({'autores': lista_de_autores})
 
@app.route('/autores/<int:id_autor>', methods=['GET'])
def obter_autor_por_id(id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify({'mensagem':'Autor não encontrado!'})
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor
    autor_atual['nome'] = autor.nome
    autor_atual['email'] = autor.email
    return jsonify({'autor': autor_atual})
 
@app.route('/autores', methods=['POST'])
def novo_autor():
    novo_autor = request.get_json()
    autor = Autor(nome=novo_autor['nome'], senha=novo_autor['senha'], email=novo_autor['email'])
    db.session.add(autor)
    db.session.commit()
    return jsonify({'mensagem':'Usuário criado com sucesso!'}, 200)
 
@app.route('/autores/<int:id_autor>', methods=['PUT'])
def alterar_autor(id_autor):
    usuario_a_alterar = request.get_json()
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify({'mensagem':'Este usuário não foi encontrado.'})
    try:
        if usuario_a_alterar['nome']:
           autor.nome = usuario_a_alterar['nome']
    except:
        pass
    try:
        if usuario_a_alterar['email']:    
           autor.email = usuario_a_alterar['email']
    except:
        pass
    try:
        if usuario_a_alterar['senha']:    
           autor.senha = usuario_a_alterar['senha']
        db.session.commit()
    except:
        pass
    return jsonify({'mensagem':'Usuário alterado com sucesso!'})
 
@app.route('/autores/<int:id_autor>', methods=['DELETE'])
def excluir_autor(id_autor):
    autor_existente = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor_existente:
        return jsonify({'mensagem':'Este autor não foi encontrado.'})
    db.session.delete(autor_existente)
    db.session.commit()
    return jsonify({'mensagem':'Autor excluído com sucesso!'})
 
app.run(port=5000, host='localhost', debug=True)