import boto3
import json
import os
import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

session = requests.Session()
GENRES_DESEJADOS = [35, 16]  # Comedy, Animation
TMDB_API_KEY = "36211654b2fd075c9f34f5f7b7827f9e"
MOVIES_CSV_KEY= "./movies.csv"
SERIES_CSV_KEY = "./series.csv"
# --------- LER DADOS DO CSV ---------
def ler_csv_s3(key, ano_minimo=2021):
    print("Lendo arquivos CSV...")
    df = pd.read_csv(key, sep="|", dtype=str)
    
    # remove nulos e duplicados
    df = df.dropna(subset=["id"]).drop_duplicates(subset=["id"])

    df["anoLancamento"] = pd.to_numeric(df["anoLancamento"], errors="coerce")
    df = df[df["anoLancamento"] >= ano_minimo]
    
    return df["id"].tolist()

# --------- RELACIONA ID do CSV com IDs do TMDB ---------
def buscar_tmdb_id(imdb_id):
    """
    Usa o endpoint /find/{external_id} para localizar correspondência no TMDB
    Retorna JSON da resposta ou None em caso de erro.
    """
    url = f"https://api.themoviedb.org/3/find/{imdb_id}"
    parametros={
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "external_source": "imdb_id"
    }

    # Tratamento de Exceções (Erro de Requisição, Busca e de Valores)
    try:
        resp = session.get(url, params=parametros, timeout=10)
        if resp.status_code != 200:
            return None
        data = resp.json()

        if data.get("movie_results"):
            return "movie", data["movie_results"][0]["id"]

        if data.get("tv_results"):
            return "tv", data["tv_results"][0]["id"]
    except:
        return None
    return None


# --------- CAPTURAR DETALHES DOS FILMES/SÉRIES DOS GÊNEROS ---------
def pegar_detalhes(endpoint, tmdb_id):
    """
    Busca detalhes completos do item no TMDB.
    endpoint: 'movie' ou 'tv'
    """
    url = f"https://api.themoviedb.org/3/{endpoint}/{tmdb_id}"
    parametros = {"api_key": TMDB_API_KEY}

    try:
        resposta = session.get(url, params=parametros, timeout=10)
        if resposta.status_code != 200:
            return {}
        try:
            return resposta.json()
        except ValueError:
            return {}
    except requests.RequestException as e:
        print(f"[ERROR] RequestException detalhes {endpoint}/{tmdb_id}: {e}")
        return {}




def filtrar_dados(imbd_ids, endpoint, max_workers=15):
    print(f"[LOADING...] Processando {endpoint} em paralelo...")
    resultado_final = []

    # função interna que processa um único id (mantém tudo dentro de filtrar_dados)
    def _processar_um_id(imdb_id):
        # --------- RELACIONA ID do CSV com IDs do TMDB ---------
        resultado = buscar_tmdb_id(imdb_id)
        if not resultado:
            # retorna uma tupla para possibilitar logs fora se quiser
            return None
        tipo, tmdb_id = resultado  # resultado = ("movie"|"tv", 12345)
        if tipo != endpoint:
            return None

        # --------- CAPTURAR DETALHES DOS FILMES/SÉRIES DOS GÊNEROS ---------
        detalhes = pegar_detalhes(tipo, tmdb_id)
        if not detalhes:
            return None

        generos = {
                    g["id"] for g in detalhes.get("genres", [])
                  }
        if not generos.intersection(GENRES_DESEJADOS):
            return None

        return {
            "imdb_id": imdb_id,
            "tmdb_id": tmdb_id,
            "adult": detalhes.get("adult"),
            "homepage": detalhes.get("homepage"),
            "belongs_to_collection": detalhes.get("belongs_to_collection") if tipo == "movie" else None,
            "popularity": detalhes.get("popularity"),
            "original_language": detalhes.get("original_language"),
        }

    # ThreadPoolExecutor dispara várias requisições ao mesmo tempo
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # agenda todas as tarefas; 
        # chave do dict é Future, valor é imdb_id (para debug)
        futures = {executor.submit(_processar_um_id, imdb_id): imdb_id for imdb_id in imbd_ids}

        for i, future in enumerate(as_completed(futures), start=1):
            try:
                res = future.result()
                if res:
                    resultado_final.append(res)
                else:
                    # opcional: log quando não há resultado (mantendo comportamento anterior)
                    # imdb = futures[future]; print(f"[WARNING] Nenhum resultado para {imdb}")
                    pass
            except Exception as e:
                imdb = futures.get(future)
                print(f"[ERROR] Falha ao processar {imdb}: {e}")

            # log de progresso a cada 100 itens (ajuste conforme desejar)
            if i % 100 == 0:
                print(f"[PROGRESS] {i}/{len(imbd_ids)} processados")

    return resultado_final






def salvar_no_s3(dados, caminho):
    if not dados:                                               # impede dados nulos
        print("[WARNING] Nenhum dado para upload")
        return
    df = pd.DataFrame(dados)
    
    # ALTERAÇÃO AQUI: 
    # orient="records" coloca cada objeto em uma lista
    # lines=True salva cada objeto em uma nova linha (padrão ouro para Spark/Big Data)
    df.to_json(caminho, orient="records", lines=True)

    print(f"[UPLOAD] {os.path.basename(caminho)}")



if __name__ == "__main__":
    movies_ids = ler_csv_s3("./movies.csv", ano_minimo=2022)
    series_ids = ler_csv_s3("./series.csv", ano_minimo=2022)

    filmes = filtrar_dados(movies_ids, "movie")
    path_filmes = "./movies.json"
    print(f"[INFO] {len(movies_ids)} filmes carregados do CSV")
    
    series = filtrar_dados(series_ids, "tv")
    path_series = "./series.json"
    print(f"[INFO] {len(series_ids)} séries carregadas do CSV")

    salvar_no_s3(filmes, path_filmes)
    salvar_no_s3(series, path_series)
    print("[FINISH] Upload finalizado com sucesso!")
