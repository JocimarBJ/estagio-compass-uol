from pyspark.sql.functions import col, trim, lower
from pyspark.sql import types as ty
import re
from pyspark.sql import functions as F
from pyspark.sql.functions import col, trim, lower
from pyspark.sql import types as ty
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("teste").getOrCreate()

dados_csv_movies = spark.read.format("csv").option("header", True).option("sep", "|").load("./1-raw/movies.csv")
dados_csv_series = spark.read.format("csv").option("header", True).option("sep", "|").load("./1-raw/series.csv")

# Converte para DataFrame e limpa o lixo "\N" transformando em Nulos.
dados_csv_movies = dados_csv_movies.replace("\\N", None)
dados_csv_series = dados_csv_series.replace("\\N", None)

# =========== PADRONIZAR COLUNAS EM SNAKE_CASE===========
def strings_snake_case(nome):
    # insere um underscore antes de cada letra maiuscula e passa tudo para  minusculo
    # Ex: tituloPrincipal -> titulo_principal
    expressao = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', nome)

    # expressão dois é para casos como "idIMDB" ou "titulo2022lancamento"
    # onde tem mais de uma letra maiuscula seguida ou numeros. Ele insere um underscore entre a numero/letra minúscula e a maiúscula, mas não entre as letras maiúsculas
    expressao = re.sub('([a-z0-9])([A-Z])', r'\1_\2', expressao).lower()

    # Retira espaços e pontos se houver, substitui por _
    expressao = re.sub(r'[\s\.]+', '_', expressao).lower()

    return expressao.lower()

# lista de mapeamento: (nome_antigo, nome_novo)
mapeamento_colunas_movies = [(c, strings_snake_case(c)) for c in dados_csv_movies.columns]
mapeamento_colunas_series = [(c, strings_snake_case(c)) for c in dados_csv_series.columns]

# O select renomeará tudo de uma vez
# O .alias() aqui serve para dar o novo nome (snake_case)
df_movies_trusted = dados_csv_movies.select([col(velho).alias(novo) for velho, novo in mapeamento_colunas_movies])
df_series_trusted = dados_csv_series.select([col(velho).alias(novo) for velho, novo in mapeamento_colunas_series])

# =========== CASTING DE TIPOS ===========
# Filmes
df_movies_trusted = df_movies_trusted \
    .withColumn("ano_lancamento", col("ano_lancamento").cast(ty.IntegerType())) \
    .withColumn("tempo_minutos", col("tempo_minutos").cast(ty.IntegerType())) \
    .withColumn("nota_media", col("nota_media").cast(ty.DoubleType())) \
    .withColumn("numero_votos", col("numero_votos").cast(ty.IntegerType())) \
    .withColumn("ano_nascimento", col("ano_nascimento").cast(ty.IntegerType())) \
    .withColumn("ano_falecimento", col("ano_falecimento").cast(ty.IntegerType()))

# Series
df_series_trusted = df_series_trusted \
    .withColumn("ano_lancamento", col("ano_lancamento").cast(ty.IntegerType())) \
    .withColumn("ano_termino", col("ano_termino").cast(ty.IntegerType())) \
    .withColumn("tempo_minutos", col("tempo_minutos").cast(ty.IntegerType())) \
    .withColumn("nota_media", col("nota_media").cast(ty.DoubleType())) \
    .withColumn("numero_votos", col("numero_votos").cast(ty.IntegerType())) \
    .withColumn("ano_nascimento", col("ano_nascimento").cast(ty.IntegerType())) \
    .withColumn("ano_falecimento", col("ano_falecimento").cast(ty.IntegerType()))

# Também poderia ser usado inferSchema, mas como o dataset é grande, preferi fazer o casting manualmente para evitar lentidão no processo de leitura do arquivo
# Além de evitar que o Spark leia alguma coluna como string por conta de algum valor atípico, como "NA" ou "null", e acabe causando problemas na hora de fazer análises ou cálculos com essas colunas

# =========== PADRONIZACAO DE STRINGS ===========
def padronizar_strings(dataset):
    padronizar = [
        lower(trim(col(c))).alias(c) if t == "string" else col(c)
        for c, t in dataset.dtypes
    ]
    return padronizar
# "c" representa o nome da coluna
# "t" representa o tipo da coluna
# O loop percorre a tabela. Se for do tipo string, remove espaços e deixa minúsculo
# Senão for string, ele mantém sem alterar
# O .alias(c) é para forçar o Spark a manter o nome original da coluna, já que o lower e trim criam uma nova coluna com o nome da função aplicada

df_movies_trusted = df_movies_trusted.select(*padronizar_strings(df_movies_trusted)).dropDuplicates()
df_series_trusted = df_series_trusted.select(*padronizar_strings(df_series_trusted)).dropDuplicates()

# ========= ESCRITA NO S3 (PARQUET) CSV ==========
# df_movies_trusted.write.mode("overwrite").format("parquet").save("./2-trusted/local/parquet/movies")
# df_series_trusted.write.mode("overwrite").format("parquet").save("./2-trusted/local/parquet/series")






# ===================================== JSON ========================

dados_json_movies = spark.read.format("json").option("multiline", False).load("./1-raw/movies.json")
dados_json_series = spark.read.format("json").option("multiline", False).load("./1-raw/series.json")

df_movies_trusted_json = dados_json_movies.select("imdb_id", "tmdb_id", "popularity", "original_language", "adult", "belongs_to_collection", "homepage")
df_series_trusted_json = dados_json_series.select("imdb_id", "tmdb_id", "popularity", "original_language", "adult", "homepage")

df_movies_trusted_json = dados_json_movies.withColumn("tmdb_id", col("tmdb_id").cast("int"))
df_series_trusted_json = dados_json_series.withColumn("tmdb_id", col("tmdb_id").cast("int"))

def padronizar_strings(dataset):
    padronizar = [
        lower(trim(col(c))).alias(c) if t == "string" else col(c)
        for c, t in dataset.dtypes
    ]
    return padronizar
df_movies_trusted_json = df_movies_trusted_json.select(*padronizar_strings(df_movies_trusted_json))
df_series_trusted_json = df_series_trusted_json.select(*padronizar_strings(df_series_trusted_json))

# ========= ESCRITA NO S3 (PARQUET) ==========
# Prepara para salvar Filmes na subpasta /movies/
df_movies_trusted_json.write.mode("overwrite").format("parquet").save("./2-trusted/tmdb/parquet/movies")
df_series_trusted_json.write.mode("overwrite").format("parquet").save("./2-trusted/tmdb/parquet/series")