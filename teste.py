from model.cadastro import cadastro_usuario
from model.musica import adicionar_musica, excluir_musica, rec_musicas
from model.usuario_model import autenticar_usuario


retorne = autenticar_usuario("Hellion", "ilymyhuband")
print(retorne)


