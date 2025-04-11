from flask import Flask, render_template, request, redirect
from BancoDeDados import CriarBanco
from Restaurante import BancoRestaurante, RestaurantesCadastrar, BuscarRestaurante, EditarRestaurante, DeletarRestaurante
from RestauranteAvaliacao import BancoAvaliacaoRestaurante, AvaliarRestaurante, BancoMediaAvaliacoes, BancoComentarios
import webview


app = Flask(__name__) # Criando a instancia do Flask

#Configurar janela do pyview
windows = webview.create_window('BestMeals', app, width = 1900, height=900, resizable=True, confirm_close=False)

# Criando Tabelas
CriarBanco()

# Definindo a rota para a página inicial
@app.route('/')
def OOhomepage():
    return render_template("Menu.html")

#Rota para o menu de restaurantes
@app.route('/Restaurantes')
def OOFuncaoRestaurante():
    TodosOsRestaurantes = BancoRestaurante()
    return render_template("Restaurantes.html", TodosOsRestaurantes=TodosOsRestaurantes)

#Cadastrar Restaurante
@app.route('/Restaurantes/Cadastrar')
def OORestaurantesCadastrar():
    return render_template("Restaurante-Cadastrar.html")

@app.route('/Restaurantes/Cadastrar/Confirmado', methods=['POST'])
def OORestaurantesCadastrarConfirmado():
    return RestaurantesCadastrar()

#Editar Restaurante
@app.route("/Restaurante/Editar/<NomeRestaurante>") #Envia o nome do restaurante para a função
def OOEditarRestaurante(NomeRestaurante):
    NomeRestaurante = BuscarRestaurante(NomeRestaurante)
    return render_template("Restaurante-Editar.html", NomeRestaurante=NomeRestaurante)

@app.route("/Restaurante/Editar", methods=["POST"]) # Envia os dados do restaurante para a função EditarProduto
def OOEditarRestaurante2():
    NovoNomeRestaurante = request.form["NovoNomeRestaurante"]
    NovoEndereco = request.form["NovoEndereco"]
    NovoCidade = request.form["NovoCidade"]
    NovoEstado = request.form["NovoEstado"]
    NovoCEP = request.form["NovoCEP"]
    DescricaoAntiga = request.form["DescricaoAntiga"]
    return EditarRestaurante(NovoNomeRestaurante, NovoEndereco, NovoCidade, NovoEstado, NovoCEP, DescricaoAntiga)

#Deletar Restaurante
@app.route("/Restaurante/Deletar/<NomeRestaurante>") #Envia o nome do restaurante para a função
def OODeletarRestaurante(NomeRestaurante):
    return DeletarRestaurante(NomeRestaurante)

#Avaliar Restaurante
@app.route("/Restaurante/Avaliar/<NomeRestaurante>") #Envia o nome do restaurante para a função
def OOAvaliarRestaurante(NomeRestaurante):
    NomeRestaurante = BuscarRestaurante(NomeRestaurante)
    return render_template("Restaurante-Avaliar.html", NomeRestaurante=NomeRestaurante)

@app.route("/Restaurante/Avaliar", methods=["POST"]) # Envia os dados do restaurante para a função EditarProduto
def OOAvaliarRestaurante2():
    NomeRestaurante2 = request.form["NomeRestaurante2"]
    Avaliação = request.form["Avaliação"]
    Comentarios = request.form["Comentarios"]
    return AvaliarRestaurante(NomeRestaurante2, Avaliação, Comentarios)


#Rota para o menu de Consultar Avaliações
@app.route('/Restaurantes/Consultar')
def OORestaurantesConsultar():
    TabelaAvaliacaoRestaurante = BancoAvaliacaoRestaurante()
    return render_template("Restaurante-Consultar.html", TabelaAvaliacaoRestaurante=TabelaAvaliacaoRestaurante)

#Rota para ver as avaliações de um restaurante
@app.route("/Restaurante/VerAvaliacoes/<NomeRestaurante>") #Envia o nome do restaurante para a função
def OOVerAvaliacoes(NomeRestaurante):
    MediaAvaliacoes = BancoMediaAvaliacoes(NomeRestaurante)
    Comentarios = BancoComentarios(NomeRestaurante)
    return render_template("Restaurante-VerAvaliacoes.html", MediaAvaliacoes=MediaAvaliacoes, Comentarios=Comentarios)


if __name__ == "__main__":
    webview.start()
    # app.run(debug=True) # Executa o Flask em modo debug para desenvolvimento