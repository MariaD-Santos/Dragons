from flask import Flask, render_template, request
import mysql.connector
from model.musica import adicionar_musica, excluir_musica, rec_musicas
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

@app.route("/musica/post", methods = ["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("musica")
    cantor = request.form.get("cantor")
    genero = request.form.get("genero")
    imagem = request.form.get("imagem")
    duracao = request.form.get("duracao")

    if adicionar_musica(cantor,nome_musica,duracao,imagem,genero):
        return("/admin")
    else:
        return "Erro ao adicionar a música!"
    
@app.route("/musica/get", methods = ["GET"])
def api_deletar_musica():
    codigo = request.form.get("codigo")

    if excluir_musica(codigo):
        return("música excluída")
    else:
        return "Erro ao excluir música"
if __name__ == "__main__":
    app.run(debug=True)