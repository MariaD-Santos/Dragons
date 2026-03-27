USE MusicTube;

INSERT INTO `MusicTube`.`genero`
(`nome`,
`icone`,
`cor`)
VALUES
("Jazz", "","blue"),
("Metal", "","red"),
("Eletrônica", "","pink"),
("Kpop","","orange"),
("Rap","","black"),
("Synthwave","","purple");


INSERT INTO `MusicTube`.`musica`
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
"Metal"),
("Friday night funkin",
"05:15",
"Release",
"https://64.media.tumblr.com/d0fefaeaad4a06e6b7246381d950bb44/e77f9ece3ba96460-e7/s1280x720/8620ee11a83815da4ef6ce8c335654b3207d3a3f.jpg",
"Eletrônica");