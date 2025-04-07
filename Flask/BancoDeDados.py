from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def CriarBanco():
    def CriarTabelaRefeicao():
        with sqlite3.connect('DadosBestMeal.db') as banco:
            cursor = banco.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Refeicao (
                NomeRefeicao TEXT NOT NULL PRIMARY KEY,
                NomeRestaurante TEXT NOT NULL,
                Preco REAL NOT NULL,
                Ingredientes TEXT NOT NULL,
                FOREIGN KEY (NomeRestaurante) REFERENCES Restaurante(NomeRestaurante)
            )""")

    def CriarTabelaAvaliacaoRefeicao():
        with sqlite3.connect('DadosBestMeal.db') as banco:
            cursor = banco.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS AvaliacaoRefeicao (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NomeRefeicaoAvaliacao TEXT NOT NULL,
                Avaliacao REAL NOT NULL,
                Comentarios TEXT NOT NULL,
                FOREIGN KEY (NomeRefeicaoAvaliacao) REFERENCES Refeicao(NomeRefeicao)
            )""")

    def CriarTabelaRestaurante():
        with sqlite3.connect('DadosBestMeal.db') as banco:
            cursor = banco.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Restaurante (
                NomeRestaurante TEXT NOT NULL PRIMARY KEY,
                Endereco TEXT NOT NULL,
                Cidade TEXT NOT NULL,
                Estado TEXT NOT NULL,
                CEP TEXT NOT NULL
            )""")

    def CriarTabelaAvaliacaoRestaurante():
        with sqlite3.connect('DadosBestMeal.db') as banco:
            cursor = banco.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS AvaliacaoRestaurante (
                NomeRestauranteAvaliacao TEXT NOT NULL,
                Avaliacao REAL NOT NULL,
                Comentarios TEXT NOT NULL,
                FOREIGN KEY (NomeRestauranteAvaliacao) REFERENCES Restaurante(NomeRestaurante) ON DELETE CASCADE ON UPDATE CASCADE
            )""")

    # Chamar as funções de criação de tabelas
    CriarTabelaRefeicao()
    CriarTabelaAvaliacaoRefeicao()
    CriarTabelaRestaurante()
    CriarTabelaAvaliacaoRestaurante()