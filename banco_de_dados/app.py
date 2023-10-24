import sqlite3

# criando banco de dados
with sqlite3.connect('artistas.db') as conexao:  
    # criar uma conexão com o banco de dados
    sql = conexao.cursor()
    
    # Rodar comando SQL
    sql.execute('create table banda(nome text, estilo text, membros interger);') 
    # Após os passos ACIMA, um arquivo artistas.db será criado
    
    # Exemplo de inserir dados
    sql.execute('insert into banda(nome, estilo, membros) values ("Banda 1", "rock", 3)')
    
    # Exemplo de usar dados em minha aplicação em um comando sql
    nome = input('Digite o nome da banda ')
    estilo = input('Digite o estilo da banda ')
    quantidade_integrantes = int(input('Quantidade de integrantes da banda '))
    
    sql.execute('insert into banda values(?,?,?)', [nome, estilo, quantidade_integrantes])
    # Acima, as interrogações serão subsituidas por nome, estilo, quantidade_integrantes, na ordem.
    
    # Para salvar as alterações acima na linha 20
    conexao.commit()
    
    # para exibir dados no console python
    bandas = sql.execute('select * from banda;')
    for banda in bandas:
        print(banda)
        
        