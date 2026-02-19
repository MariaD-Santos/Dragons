from database.conexao import conectar

def rec_musicas():
    #passo 1 e 2
    conexao, cursor = conectar()

    # executando a consulta
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")

    # recuperando os dados
    musicas = cursor.fetchall()
    
    # fechando conexão
    conexao.close()

    return musicas