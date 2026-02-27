from flask import Flask, redirect, render_template, request
import mysql.connector
from model.musica import adicionar_musica, alterar_musica, excluir_musica, rec_musicas
from model.genero import rec_generos

app = Flask(__name__)

@app.route("/")

@app.route("/home", methods=["GET"])
def pagina_principal():

    generos= rec_generos()
    musicas= rec_musicas(True)

    return render_template("principal.html", musicas= musicas, generos = generos)

@app.route("/login")
def pagina_login():
    return render_template("cadastro.html")


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
        return redirect("/admin")
    else:
        return "Erro ao adicionar a música!"
    
@app.route("/musica/delete/<codigo>")
def api_deletar_musica(codigo):
    excluir_musica(codigo)

    return redirect("/admin")

@app.route("/musica/alterar/<codigo>/<ativo>")
def api_alterar_musica(codigo,ativo):
    alterar_musica(codigo, ativo)

    return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)