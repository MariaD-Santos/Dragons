from flask import Flask, render_template
import mysql.connector
from model.musica import rec_musicas
from model.genero import rec_generos

app = Flask(__name__)

@app.route("/")

@app.route("/home", methods=["GET"])
def pagina_principal():

    generos= rec_generos()
    musicas= rec_musicas()

    return render_template("principal.html", musicas= musicas, generos = generos)

@app.route("/admin")
def pagina_adm():
    musicas = rec_musicas()
    generos = rec_generos()
    return render_template("administracao.html", musicas = musicas, generos = generos)

if __name__ == "__main__":
    app.run(debug=True)