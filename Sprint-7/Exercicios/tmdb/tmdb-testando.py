# Para rodar localmente execute: py -m pip install requests pandas

# Testando rapidamente as credenciais e a biblioteca
import requests
import pandas as pd
from IPython.display import display

# Chave API do TMDB
api_key = "36211654b2fd075c9f34f5f7b7827f9e"

# URL de acesso à API para obter os filmes mais bem avaliados
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&amp;language=pt-BR"

# Fazendo a requisição e processando os dados
response = requests.get(url)
data = response.json()
filmes = []

# Iterando sobre os resultados e criando um dicionário para cada filme
for movie in data['results']:
    df = {
        'Titulo': movie['title'],
        'Data de lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos': movie['vote_average']
        }
    
    # Adicionando o dicionário ao DataFrame
    filmes.append(df)

# Criando um DataFrame para exibir os dados
df = pd.DataFrame(filmes)
display(df)