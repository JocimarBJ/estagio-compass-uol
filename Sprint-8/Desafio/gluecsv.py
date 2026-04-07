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

# ====== LEITURA E LIMPEZA DE NULOS ========
dynamic_frame_movies = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file_movies]},
    format="csv",
    format_options={"withHeader": True, "separator":"|"},
)
dynamic_frame_series = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file_series]},
    format="csv",
    format_options={"withHeader": True, "separator":"|"},
)

# Converte para DataFrame e limpa o lixo "\N" transformando em Nulos.
df_movies = dynamic_frame_movies.toDF().replace("\\N", None)
df_series = dynamic_frame_series.toDF().replace("\\N", None)

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
mapeamento_colunas_movies = [(c, strings_snake_case(c)) for c in df_movies.columns]
mapeamento_colunas_series = [(c, strings_snake_case(c)) for c in df_series.columns]

# O select renomeará tudo de uma vez
# O .alias() aqui serve para dar o novo nome (snake_case)
df_movies_trusted = df_movies.select([col(velho).alias(novo) for velho, novo in mapeamento_colunas_movies])
df_series_trusted = df_series.select([col(velho).alias(novo) for velho, novo in mapeamento_colunas_series])

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