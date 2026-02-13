from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")

@app.route("/home", methods=["GET"])
def pagina_principal():

    # conectando no BCD
    conexao = mysql.connector.connect(
        host="localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "MusicTube"
    )

    # criando o cursos
    cursor = conexao.cursor(dictionary=True)  # entrega os valores das colunas

    # executando a consulta
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")

    # recuperando os dados
    musicas = cursor.fetchall()
    
    # executando a consulta do genero
    cursor.execute("SELECT nome, icone, cor FROM genero;")

    generos = cursor.fetchall()
    # fechando a conexão
    conexao.close()

    return render_template("principal.html", musicas= musicas, generos = generos)

@app.route("/admin")
def pagina_adm():
    return render_template("administracao.html")

if __name__ == "__main__":
    app.run(debug=True)