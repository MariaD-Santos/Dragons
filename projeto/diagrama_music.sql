create database IF NOT EXISTS MusicTube;

use MusicTube;

CREATE TABLE IF NOT EXISTS genero (
 nome VARCHAR(30) NOT NULL PRIMARY KEY,
 descricao VARCHAR(100),
 icone CHAR(100),
 cor CHAR(10)
);


CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY auto_increment,
 cantor VARCHAR(50),
 genero VARCHAR(30),
 duracao TIME,
 nome VARCHAR(50),
 url_imagem VARCHAR(255),
 nome_genero VARCHAR(30),
 CONSTRAINT fk_musica_genero FOREIGN KEY (nome_genero) REFERENCES genero (nome)
);


