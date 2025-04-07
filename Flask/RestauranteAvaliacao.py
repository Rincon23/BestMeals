from flask import redirect
import sqlite3

# Avaliar restaurante
def AvaliarRestaurante(NomeRestaurante2, Avaliacao, Comentarios):
    try:
        banco = sqlite3.connect('DadosBestMeal.db')
        cursor = banco.cursor()

        cursor.execute("INSERT INTO AvaliacaoRestaurante ( NomeRestauranteAvaliacao, Avaliacao, Comentarios) VALUES (?, ?, ?)", 
                       (NomeRestaurante2, Avaliacao, Comentarios))

        banco.commit() 
        banco.close()
        print("Restaurante avaliado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao avaliar o restaurante: ", erro)

    return redirect("/Restaurantes")

#Seleciona Todas as avaliações dos restaurantes
def BancoAvaliacaoRestaurante():
    conn = sqlite3.connect("DadosBestMeal.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AvaliacaoRestaurante GROUP BY NomeRestauranteAvaliacao")
    TabelaAvaliacaoRestaurante = cursor.fetchall()
    conn.close()
    return TabelaAvaliacaoRestaurante

#Seleciona as médias das avaliações do restaurante especificado
def BancoMediaAvaliacoes(NomeRestauranteAvaliacao):
    conn = sqlite3.connect("DadosBestMeal.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT *, AVG(Avaliacao) as MediaAvaliacoes
                   FROM AvaliacaoRestaurante 
                   WHERE NomeRestauranteAvaliacao = ?
                   GROUP BY NomeRestauranteAvaliacao
                   """, (NomeRestauranteAvaliacao,))
    MediaAvaliacoes = cursor.fetchall()
    conn.close()
    return MediaAvaliacoes

#Seleciona os comentários e avaliações do restaurante especificado
def BancoComentarios(NomeRestauranteAvaliacao):
    conn = sqlite3.connect("DadosBestMeal.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT Comentarios, Avaliacao
                   FROM AvaliacaoRestaurante 
                   WHERE NomeRestauranteAvaliacao = ?
                   """, (NomeRestauranteAvaliacao,))
    Comentarios = cursor.fetchall()
    conn.close()
    return Comentarios