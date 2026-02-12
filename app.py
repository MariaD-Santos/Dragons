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

    return render_template("principal.html")

@app.route("/admin")
def pagina_adm():
    return render_template("administracao.html")

if __name__ == "__main__":
    app.run(debug=True)