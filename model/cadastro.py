from database.conexao import conectar

def cadastro_usuario(usuario:str, senha:str):
    try:
        conexao, cursor =  conectar()

        cursor.execute(""" INSERT INTO cadastro(usuario, senha) 
                            VALUES(%s,%s)""",
                            [usuario, senha])
        
        conexao.commit()
        conexao.close()

        return True
        
    except Exception as e:
        print (e)
        return False