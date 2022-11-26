# Como usar os 4 principais comandos(verbos) de uma api

import requests

from pprint import pprint   

# pprint vai deixar mais legível o resultados de uma api

# get - permite obter informações de uma api

# entrar no site https://jsonplaceholder.typicode.com/ e descer até 'todos' e pegar este link:
# https://jsonplaceholder.typicode.com/todos

resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())  # json é o formato mais comum que as api trabalham

# Ao dar play no terminal, vai aparecer uma lista de coisas a fazer

# get com id = vai pegar as coisas a fazer somente via id, vai filtrar
resultado_get_com_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')  # quer dizer que vamos obter a segunda tarefa
pprint(resultado_get_com_id.json())

nova_tarefa = {'completed': False,
 'title': 'lavar o carro',
 'userId': 1}


# post - criar um novo recurso
resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos', nova_tarefa)

pprint(resultado_post.json())

# put - serve para alterar um recurso existente

tarefa_alterada = {'completed': False,
 'title': 'lavar a moto',
 'userId': 1}

resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2', tarefa_alterada)

pprint(resultado_put.json())

# Delete - excluir um recurso

resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())
