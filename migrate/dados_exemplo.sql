USE MusicTube;

INSERT INTO `musictube`.`genero`
(`nome`,
`icone`,
`cor`)
VALUES
("Jazz", "","blue"),
("Metal", "","red"),
("Eletrônica", "","pink");


INSERT INTO `musictube`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_imagem`,
`nome_genero`)
VALUES
("Friday night funkin",
"02:02",
"fnf WEEKEND",
"https://i.pinimg.com/736x/b0/29/40/b0294070012826dbff04fe015beacca1.jpg",
"Eletrônica"),
("Slipknot",
"05:03",
"Psychosocial",
"https://cdn-images.dzcdn.net/images/artist/d1a3db36015dd98615f42a5441dcf2f5/1900x1900-000000-81-0-0.jpg",
"Metal");

