create database IF NOT EXISTS MusicTube;

use MusicTube;

CREATE TABLE IF NOT EXISTS genero (
 nome VARCHAR(30) NOT NULL PRIMARY KEY,
 icone CHAR(100),
 cor CHAR(10)
);


CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY auto_increment,
 cantor VARCHAR(50),
 duracao TIME,
 nome VARCHAR(50),
 url_imagem VARCHAR(500),
 nome_genero VARCHAR(30),
 ativo bool default 0,
 CONSTRAINT fk_musica_genero FOREIGN KEY (nome_genero) REFERENCES genero (nome)
);
