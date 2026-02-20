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

def adicionar_musica(cantor:str, nome_musica:str, duracao:str, url_imagem:str, genero:str) -> bool:
    """
    Essa função é para auxiliar o usuário a inserir novas músicas.
    """

    conexao, cursor = conectar()

    cursor.execute("""
                   INSERT INTO musica(cantor, nome, duracao, url_imagem, nome_genero) 
                   VALUES(%s,%s,%s,%s,%s);
                   """,
                   [cantor, nome_musica, duracao, url_imagem, genero]
                   )


    conexao.commit()
    conexao.close()
