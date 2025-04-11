<h1> BestMeals </h1>
<p>
  <img src="Imagens/ImagemProjeto.png" width="500">
</p>

---

## 📚 Sumário

### [📌 Sobre o Projeto](#-sobre-o-projeto)
### [🧰 Tecnologias Utilizadas](#-tecnologias-utilizadas)
### [💻 Como rodar o programa (sem usar código)](#-como-rodar-o-programa-sem-usar-código)
### [👨‍💻 Como rodar o código (modo desenvolvedor)](#-como-rodar-o-código-modo-desenvolvedor)
### [📁 Estrutura de Pastas e Arquivos](#-estrutura-de-pastas-e-arquivos)
### [📷 Imagens do sistema](#-imagens-do-sistema)
### [📞 Contato e Créditos](#-contato-e-créditos)

---

## 📌 Sobre o projeto
### BestMeals é um sistema simples e funcional de cadastro e avaliação de itens. Foi idealizado inicialmente para restaurantes, mas sua estrutura permite fácil adaptação para avaliar qualquer coisa – como filmes, livros, produtos, entre outros.

### 💡 Objetivo principal: desenvolver um projeto prático que me permitisse demonstrar habilidades em programação e, ao mesmo tempo, aprender novas bibliotecas e funcionalidades, como o uso do Flask, SQLite e PyWebview.

### 🎯 O foco foi criar um sistema funcional, com boa organização de pastas e código limpo, que pudesse ser executado por qualquer pessoa, mesmo sem conhecimento técnico.

## 🧰 Tecnologias Utilizadas
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> 
<p>Linguagem principal utilizada para desenvolver toda a lógica do sistema e integração entre as partes.</p>

<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/> 

<p>Framework web responsável por gerenciar as rotas e exibir as páginas HTML de forma dinâmica.</p>

<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/> 

<p>Banco de dados leve e local usado para armazenar os dados dos restaurantes e avaliações.</p>

<img src="https://img.shields.io/badge/PyWebView-007ACC?style=for-the-badge&logo=python&logoColor=white"/>

<p>Biblioteca que permite executar a aplicação web como se fosse um programa de desktop, com uma janela nativa.</p>

<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/> 
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/> 


<p>Estruturaram e estilizaram as interfaces gráficas das páginas do sistema. Foram utilizados vários arquivos CSS para manter o estilo organizado e separado por funcionalidade.</p>

## 💻 Como rodar o programa (sem usar código)

#### ✅ 1. Baixe a pasta "Arquivo Executável"

#### ✅ 2. Execute o Arquivo "BestMeals"

    ├── Arquivo Executável <----------- BAIXE ESTA PASTA
        └── BestMeals.exe  <----------- EXECUTE ESTE ARQUIVO 
    ├── Flask
    ├── Imagens
    ├── .gitignore
    └── README.md

## 👨‍💻 Como rodar o código (modo desenvolvedor)

### ✅ 1º Passo (Instalar Python e bibliotecas):

### Instalar o Python em sua maquina

#### Baixe o Python em: https://www.python.org/

#### No terminal (CMD ou PowerShell):
    pip install Flask
---
    pip install pywebview

#### Se não funcionar, use:

    py -m pip install Flask
---
    py -m pip install pywebview

### ✅ 2º Passo — Instalar extensões no VS Code

#### No VS Code, instale:

- Python
- Python Debugger
- Pylance

### ✅ 3º Passo — Executar o projeto

#### No terminal do VS Code:
    python Flask\main.py

#### Esse comando executa o seguinte arquivo:

    ├── Arquivo Executável
    ├── Flask
    │    ├── BancoDeDados.py
    │    ├── Main.py <--------  ESTE ARQUIVO
    │    ├── Restaurante.py
    │    ├── RestauranteAvaliacao.py
    │    ├── static
    │    └── templates
    ├── Imagens
    ├── .gitignore
    └── README.md

## 📁 Estrutura de Pastas e Arquivos

### Abaixo está uma explicação da estrutura do projeto e da função de cada parte:

    ├── Arquivo Executável
    │   └── BestMeals.exe
    │       → Instalador do programa para rodar no Windows sem necessidade de abrir código.
    ├── Flask
    │   ├── BancoDeDados.py
    │       → Script responsável pela criação e manipulação do banco de dados SQLite.
    │   ├── Main.py
    │       → Arquivo principal que inicia o servidor Flask e o sistema.
    │   ├── Restaurante.py
    │       → Classe que representa os dados de um restaurante.
    │   ├── RestauranteAvaliacao.py
    │       → Classe que representa uma avaliação de restaurante.
    │   ├── static
    │   │   └── css
    │   │       → Arquivos CSS responsáveis pelo estilo visual das páginas.
    │   │       ├── Style-Restaurante-Avaliar.css
    │   │       ├── Style-Restaurante-Cadastrar.css
    │   │       ├── Style-Restaurante-Editar.css
    │   │       ├── Style-Restaurante-VerAvaliacoes.css
    │   │       └── Style.css (geral)
    │   └── templates
    │       → Páginas HTML renderizadas pelo Flask.
    │       ├── Menu.html
    │       ├── Restaurante-Avaliar.html
    │       ├── Restaurante-Cadastrar.html
    │       ├── Restaurante-Consultar.html
    │       ├── Restaurante-Editar.html
    │       ├── Restaurante-VerAvaliacoes.html
    │       └── Restaurantes.html
    │
    ├── Imagens
    |   → Imagens utilizadas na apresentação e documentação do projeto.
    │    ├── Avaliação
    │    ├── AvaliaçõesDoRestaurante
    │    ├── Cadastro
    │    ├── ImagemProjeto
    │    ├── Menu
    │    ├── TabelaComAvaliações
    │    └── TabelaRestaurantes
    │
    ├── .gitignore
    │   → Arquivo para ignorar arquivos e pastas no versionamento Git.
    │
    └── README.md
        → Arquivo de documentação do projeto (este aqui).

## 📷 Imagens do sistema

<table>
  <tr>
    <td align="center"><strong>Tela de Menu</strong></td>
    <td align="center"><strong>Tabela dos Restaurantes Cadastrados</strong></td>
  </tr>
  <tr>
    <td><img src="Imagens/Menu.png" width="400"/></td>
    <td><img src="Imagens/TabelaRestaurantes.png" width="400"/></td>
  </tr>
  <tr>
    <td align="center"><strong>Tela de Cadastro dos Restaurantes</strong></td>
    <td align="center"><strong>Tela para Avaliar</strong></td>
  </tr>
  <tr>
    <td><img src="Imagens/Cadastro.png" width="400"/></td>
    <td><img src="Imagens/Avaliação.png" width="400"/></td>
  </tr>
  <tr>
    <td align="center"><strong>Ver Avaliações dos Restaurantes</strong></td>
    <td align="center"><strong>Tela de Avaliações</strong></td>
  </tr>
  <tr>
    <td><img src="Imagens/TabelaComAvaliações.png" width="400"/></td>
    <td><img src="Imagens/AvaliaçõesDoRestaurante.png" width="400"/></td>
  </tr>
</table>

## 📞 Contato e Créditos

<h3> Desenvolvido por <a href= https://github.com/Rincon23>Enzo Rincon</a></h3>  

<p>Se você gostou do projeto, tem sugestões de melhorias ou quer trocar uma ideia sobre desenvolvimento, sinta-se à vontade para entrar em contato pelos links abaixo 👇</p>

<p>
<a href = https://www.linkedin.com/in/enzorincon>
<img src = https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white>
</a>
<a href = https://www.instagram.com/enzo.rincon>
<img src = https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white>
</a>
<a href = mailto:enzorincon2003@gmail.com>
<img src = https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white>
</a>
</p>

