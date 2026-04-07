import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, trim, lower
from pyspark.sql import types as ty
import re

# ================ CONFIG ================
# @params: [JOB_NAME], [S3_INPUT_PATH], [S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH_MOVIE','S3_INPUT_PATH_SERIES','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file_movies = args['S3_INPUT_PATH_MOVIE']
source_file_series = args['S3_INPUT_PATH_SERIES']
target_path = args['S3_TARGET_PATH']

# ====== LEITURA ========
dynamic_frame_movies = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file_movies], "recurse": True},
    format="json",
    format_options={"jsonPath": "$[*]", "multiline": True},
)
dynamic_frame_series = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file_series], "recurse": True},
    format="json",
    format_options={"jsonPath": "$[*]", "multiline": True},
)

# Converte para DataFrame
df_movies = dynamic_frame_movies.toDF()
df_series = dynamic_frame_series.toDF()

df_movies_trusted = df_movies.select("imdb_id", "tmdb_id", "popularity", "original_language", "adult", "belongs_to_collection", "homepage")
df_series_trusted = df_series.select("imdb_id", "tmdb_id", "popularity", "original_language", "adult", "homepage")

df_movies_trusted = df_movies_trusted.withColumn("tmdb_id", col("tmdb_id").cast(ty.IntegerType()))
df_series_trusted = df_series_trusted.withColumn("tmdb_id", col("tmdb_id").cast(ty.IntegerType()))

def padronizar_strings(dataset):
    padronizar = [
        lower(trim(col(c))).alias(c) if t == "string" else col(c)
        for c, t in dataset.dtypes
    ]
    return padronizar
df_movies_trusted = df_movies_trusted.select(*padronizar_strings(df_movies_trusted))
df_series_trusted = df_series_trusted.select(*padronizar_strings(df_series_trusted))

# ========= ESCRITA NO S3 (PARQUET) ==========
# Prepara para salvar Filmes na subpasta /movies/
dynamic_frame_movies_salvar = DynamicFrame.fromDF(df_movies_trusted, glueContext, "dynamic_frame_movies_salvar")
# Prepara para salvar Séries na subpasta /series/
dynamic_frame_series_salvar = DynamicFrame.fromDF(df_series_trusted, glueContext, "dynamic_frame_series_salvar")

glueContext.write_dynamic_frame.from_options(
    frame = dynamic_frame_movies_salvar,
    connection_type = "s3",
    connection_options = {"path": f"{target_path}/movies/"},
    format = "parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame = dynamic_frame_series_salvar,
    connection_type = "s3",
    connection_options = {"path": f"{target_path}/series/"},
    format = "parquet"
)

job.commit()