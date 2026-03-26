from database.conexao import conectar

def autenticar_usuario(usuario:str, senha:str):
    try:
        conexao, cursor = conectar()
        cursor.execute("""
                    SELECT usuario, senha FROM cadastro
                       WHERE usuario, senha = %s, %s
                    """, [usuario, senha])
        conexao.close()


    except Exception as e:
        print(e)
        return False