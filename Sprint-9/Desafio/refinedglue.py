import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

# ================ CONFIG ================
args = getResolvedOptions(sys.argv, ['JOB_NAME','BUCKET_NAME', 'INPUT_PATH_LOCAL', 'INPUT_PATH_TMDB', 'TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

bucket = args['BUCKET_NAME']
path_local = args['INPUT_PATH_LOCAL']
path_tmdb = args['INPUT_PATH_TMDB'] 
target_path = args['TARGET_PATH'] 

# =========================
# LEITURA e PADRONIZACAO
# =========================

df_local_movies = spark.read.parquet(f"{bucket}/{path_local}/movies/") \
    .withColumnRenamed("id", "imdb_id") \
    .withColumnRenamed("titulo_pincipal", "titulo_principal") \
    .filter(F.lower(F.col("genero")).contains("comedy") | F.lower(F.col("genero")).contains("animation"))

# Filmes
df_tmdb_movies = spark.read.parquet(f"{bucket}/{path_tmdb}/movies/")

# União de Movies local + tmdb
df_movies_joined = df_local_movies.join(df_tmdb_movies, on="imdb_id", how="inner") \
    .select(
        "imdb_id",
        "tmdb_id",
        "genero",
        F.col("adult").alias("adulto"),
        "titulo_principal",
        "ano_lancamento",
        F.lit(None).alias("ano_termino"),
        F.col("popularity").alias("popularidade"),
        "nota_media",
        "numero_votos",
        F.col("belongs_to_collection.id").alias("nk_franquia"),
        F.col("belongs_to_collection.name").alias("nome_franquia")
    ).withColumn("tipo", F.lit("filme"))

# Series
df_local_series = (
    spark.read.parquet(f"{bucket}/{path_local}/series/")
    .withColumnRenamed("id", "imdb_id")
    .withColumnRenamed("titulo_pincipal", "titulo_principal")
    .filter(
        F.lower(F.col("genero")).contains("comedy") | 
        F.lower(F.col("genero")).contains("animation")
    )
)

df_tmdb_series = spark.read.parquet(f"{bucket}/{path_tmdb}/series/")

# União de Series local + tmdb
df_series_joined = df_local_series.join(df_tmdb_series, on="imdb_id", how="inner") \
    .select(
        "imdb_id",
        "tmdb_id",
        "genero",
        F.col("adult").alias("adulto"),
        "titulo_principal",
        "ano_lancamento",
        "ano_termino",
        F.col("popularity").alias("popularidade"),
        "nota_media",
        "numero_votos",
        F.lit(None).alias("nk_franquia"),
        F.lit(None).alias("nome_franquia")
    ).withColumn("tipo", F.lit("serie"))


# =========================
# UNION de Movies + Series
# =========================

df_base = df_movies_joined.unionByName(df_series_joined).cache()
# Conversão do id do IMDB para númérico
df_base = df_base.withColumn("imdb_id", F.regexp_replace("imdb_id", "tt", "").cast("int"))

# ==========================================
# 2. CRIAÇÃO DAS DIMENSÕES
# ==========================================

# Dimensão Franquia
df_dim_franquia = (
    df_base
    .filter(F.col("nk_franquia").isNotNull())
    .select("nk_franquia", "nome_franquia")
    .dropDuplicates(["nk_franquia"])
    .withColumn("sk_franquia", F.monotonically_increasing_id())
    .select("sk_franquia", "nk_franquia", "nome_franquia")
)

# Dimensão Obra
df_dim_obra = (
    df_base
    .select(
        F.col("tmdb_id").alias("nk_tmdb"),
        F.col("imdb_id").alias("nk_imdb"),
        "tipo",
        "genero",
        "adulto",
        "titulo_principal",
        "ano_lancamento",
        "ano_termino"
    )
    .dropDuplicates(["nk_imdb"])
    .withColumn("sk_obra", F.monotonically_increasing_id())
    .select(
        "sk_obra",
        "nk_tmdb",
        "nk_imdb",
        "tipo",
        "genero",
        "adulto",
        "titulo_principal",
        "ano_lancamento",
        "ano_termino"
    )
)

# Dimensão tempo
df_dim_tempo = (
    df_base
    .select(F.current_date().alias("data_completa")).distinct()
    .withColumn("sk_tempo", F.date_format("data_completa", "yyyyMMdd").cast("int"))
    .withColumn("dia_semana", F.date_format("data_completa", "EEEE"))
    .withColumn("mes", F.month("data_completa"))
    .withColumn("nome_mes", F.date_format("data_completa", "MMMM"))
    .withColumn("trimestre", F.quarter("data_completa"))
    .withColumn("semestre", F.when(F.col("mes") <= 6, 1).otherwise(2))
    .withColumn("ano", F.year("data_completa"))
    .select("sk_tempo", "data_completa", "dia_semana", "ano", "mes", "nome_mes", "trimestre", "semestre")
)

# ==========================================
# 3. CRIAÇÃO DA TABELA FATO
# ==========================================
# Pelas minhas pesquisas, a criação da tabela fato é aconselhado a ser criado por último
# Uma vez que:
# O processo ideal é definir a granularidade e criar as dimensões (obra, franquia, tempo) para, só então, estruturar a tabela fato com as chaves estrangeiras que as conectam.

df_fato_avaliacao = (
    df_base
    .dropDuplicates(["imdb_id"]) 
    # Trazer SK Obra
    .join(
        df_dim_obra
        .select("sk_obra", "nk_imdb"), 
        df_base["imdb_id"] == df_dim_obra["nk_imdb"], 
        "left"
        )
    # Trazer SK Franquia
    .join(
        F.broadcast(
            df_dim_franquia
            .select("sk_franquia", "nk_franquia"), 
            df_base["nk_franquia"] == df_dim_franquia["nk_franquia"], 
            "left"
        )
    )
    # Atribuir SK Tempo e Métricas
    .withColumn("data_extracao", F.current_date())
    .withColumn("sk_tempo", F.date_format("data_extracao", "yyyyMMdd").cast("int"))
    .withColumn("sk_avaliacao", F.monotonically_increasing_id())
    .select(
        "sk_avaliacao", "sk_obra", "sk_franquia", "sk_tempo",
        "nota_media",
        "numero_votos",
        "popularidade",
        "data_extracao"
    )
)


# ==========================================
# 4. EXTRAÇÃO
# ==========================================

def write_to_refined(df, table_name):
    target = f"{bucket}/{target_path}/{table_name}/"
    df.coalesce(1).write.mode("overwrite").parquet(target)

write_to_refined(df_dim_obra, "dim_obra")
write_to_refined(df_dim_franquia, "dim_franquia")
write_to_refined(df_dim_tempo, "dim_tempo")
write_to_refined(df_fato_avaliacao, "fato_avaliacao")

df_base.unpersist()
job.commit()