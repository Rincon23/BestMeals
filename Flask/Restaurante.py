from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

#Seleciona Todos os restaurantes
def BancoRestaurante():
    conn = sqlite3.connect("DadosBestMeal.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Restaurante")
    TabelaRestaurante = cursor.fetchall()
    conn.close()
    return TabelaRestaurante

#Mostra a página de restaurantes
@app.route("/Restaurantes/Cadastrar/Confirmado", methods=["POST"])
def RestaurantesCadastrar():
    try:
        NomeRestaurante = request.form["NomeRestaurante"]
        Endereco = request.form["Endereco"]
        Cidade = request.form["Cidade"]
        Estado = request.form["Estado"]
        CEP = request.form["CEP"]

        conn = sqlite3.connect("DadosBestMeal.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Restaurante (NomeRestaurante, Endereco, Cidade, Estado, CEP) VALUES (?, ?, ?, ?, ?)", 
                       (NomeRestaurante, Endereco, Cidade, Estado, CEP))
        conn.commit()
        conn.close()
    except sqlite3.Error as erro:
        print("Erro ao adicionar: ", erro)
    return redirect("/Restaurantes")

#Busca o restaurante pelo nome para editar, deletar ou avaliar
def BuscarRestaurante(NomeRestaurante):
    conn = sqlite3.connect("DadosBestMeal.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Restaurante WHERE NomeRestaurante = ?", (NomeRestaurante,))
    NomeRestaurante = cursor.fetchone()
    conn.close()

    return NomeRestaurante

#Editar restaurante
def EditarRestaurante(NovoNomeRestaurante, NovoEndereco, NovoCidade, NovoEstado, NovoCEP, DescricaoAntiga):
    try:
        banco = sqlite3.connect('DadosBestMeal.db')
        cursor = banco.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("UPDATE Restaurante SET NomeRestaurante = ?, Endereco = ?, Cidade = ?, Estado = ?, CEP = ? WHERE NomeRestaurante = ?", 
                       (NovoNomeRestaurante, NovoEndereco, NovoCidade, NovoEstado, NovoCEP, DescricaoAntiga))
        


        banco.commit() 
        banco.close()
        print("Restaurante atualizado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao atualizar o produto: ", erro)

    return redirect("/Restaurantes")


# Deletar restaurante
def DeletarRestaurante(NomeRestaurante): # Deletar o restaurante do banco de dados
    try:
        banco = sqlite3.connect('DadosBestMeal.db')
        cursor = banco.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("DELETE FROM Restaurante WHERE NomeRestaurante = ?", (NomeRestaurante,))
        banco.commit()
        banco.close()
        print("Restaurante deletado com sucesso!")
    except sqlite3.Error as erro:
        print("Erro ao Deletar o produto: ", erro)

    return redirect("/Restaurantes")


