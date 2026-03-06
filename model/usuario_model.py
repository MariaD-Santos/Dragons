from database.conexao import conectar

def autenticar_usuario(usuario:str, senha:str) -> list:
 
        conexao, cursor =  conectar()
        cursor.execute("""
                       SELECT usuario, senha from cadastro
                       WHERE usuario = %s and senha = %s;
                        """, [usuario,senha])
        
        usuario = cursor.fetchone()
        conexao.commit()
        conexao.close()
        return usuario