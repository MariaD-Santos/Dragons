
import mysql.connector



def conectar():
        tipo_conexao = "LOCAL"
        if tipo_conexao == "LOCAL":
            conexao = mysql.connector.connect(
                    host="localhost",
                    port = 3306,
                    user = "root",
                    password = "root",
                    database = "MusicTube"
                )
        else:
            conexao = mysql.connector.connect(
                    host="servidor-majwaw-server-welcome.a.aivencloud.com",
                    port = 11569,
                    user = "avnadmin",
                    password = "AVNS_1evNwUdL6W4JTZJ5MEM",
                    database = "MusicTube"
                )

            # criando o cursos
        cursor = conexao.cursor(dictionary=True)  # entrega os valores das colunas

        return conexao, cursor