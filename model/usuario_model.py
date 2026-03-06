from database.conexao import conectar

def autenticar_usuario(usuario:str, senha:str) -> 
    try:
        conexao, cursor =  conectar()
        cursor.execute("""
                       SELECT usuario, senha from cadastro
                       WHERE usuario = %s and senha = %s;
                        """)
        conexao.commit()
        conexao.close()
        return True
    
    except Exception as e:
        print(e)
        return False