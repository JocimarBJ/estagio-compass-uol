from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.master("local[*]").appName("teste").getOrCreate()

dfs = []
tipos = ["movies", "series"]
caminhos = ["local", "tmdb"]

# =========================
# LEITURA e PADRONIZACAO (Camada Enriched)
# =========================

df_local_movies = (
    spark.read.parquet(f"2-trusted/local/parquet/movies")
    .withColumnRenamed("id", "imdb_id")
    .withColumnRenamed("titulo_pincipal", "titulo_principal")
    .filter(
        F.lower(F.col("genero")).contains("comedy") | 
        F.lower(F.col("genero")).contains("animation")
    )
)

df_tmdb_movies = spark.read.parquet(f"2-trusted/tmdb/parquet/movies")

# Filmes
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

df_local_series = (
    spark.read.parquet(f"2-trusted/local/parquet/series")
    .withColumnRenamed("id", "imdb_id")
    .withColumnRenamed("titulo_pincipal", "titulo_principal")
    .filter(
        F.lower(F.col("genero")).contains("comedy") | 
        F.lower(F.col("genero")).contains("animation")
    )
)

df_tmdb_series = spark.read.parquet(f"2-trusted/tmdb/parquet/series")

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
# UNION
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
membro_desconhecido = spark.createDataFrame([(-1, -1, "Não se aplica")], df_dim_franquia.schema)
df_dim_franquia = df_dim_franquia.union(membro_desconhecido)

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

df_fato_avaliacao = (
    df_base
    .dropDuplicates(["imdb_id"]) 
    # Trazer SK Obra
    .join(df_dim_obra.select("sk_obra", "nk_imdb"), df_base["imdb_id"] == df_dim_obra["nk_imdb"], "left")
    # Trazer SK Franquia
    .join(df_dim_franquia.select("sk_franquia", "nk_franquia"), df_base["nk_franquia"] == df_dim_franquia["nk_franquia"], "left")
    # Atribuir SK Tempo e Métricas
    .withColumn("data_extracao", F.current_date())
    .withColumn("sk_tempo", F.date_format("data_extracao", "yyyyMMdd").cast("int"))
    .withColumn("sk_avaliacao", F.monotonically_increasing_id())
    # Garantir que não existam nulos
    .withColumn("sk_franquia", F.coalesce(F.col("sk_franquia"), F.lit(-1)).cast("long"))
    .select(
        "sk_avaliacao", "sk_obra", "sk_franquia", "sk_tempo",
        "nota_media",
        "numero_votos",
        "popularidade",
        "data_extracao"
    )
)


# ==========================================
# 4. EXIBIÇÃO E FINALIZAÇÃO
# ==========================================

print("=========FATO_AVALIACAO:===========")
df_fato_avaliacao.write.mode("overwrite").format("parquet").save("./3-refined/fato_avaliacao")

print("===========DIM_OBRA:=========")
df_dim_obra.write.mode("overwrite").format("parquet").save("./3-refined/dim_obra")

print("=========DIM_FRANQUIA:===========")
df_dim_franquia.write.mode("overwrite").format("parquet").save("./3-refined/dim_franquia")

print("========DIM_TEMPO=========")
df_dim_tempo.write.mode("overwrite").format("parquet").save("./3-refined/dim_tempo")

for item in [df_fato_avaliacao, df_dim_obra, df_dim_franquia, df_dim_tempo]:
    item.show(truncate=False)

# Liberar cache
df_base.unpersist()