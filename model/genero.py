from database.conexao import conectar

def rec_generos():

    conexao, cursor = conectar()
    # executando a consulta do genero
    cursor.execute("SELECT nome, icone, cor FROM genero;")

    generos = cursor.fetchall()

    conexao.close()
    
    return generos