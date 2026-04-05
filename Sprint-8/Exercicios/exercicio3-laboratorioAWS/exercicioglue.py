import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from awsglue.dynamicframe import DynamicFrame

# @params: [JOB_NAME], [S3_INPUT_PATH], [S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator":","},
)

df = dynamic_frame.toDF()

df.printSchema()

# Padronizando tipos para evitar ponto flutuante
df = df.withColumn("total", F.col("total").cast("int"))
df = df.withColumn("ano", F.col("ano").cast("int"))

# Deixando nome da Coluna "nome" e seus dados em maiúsculo, conforme solicitado
df = df.withColumn("nome", F.upper(F.col("nome")))
df = df.withColumnRenamed("nome", "NOME")

# Total de linhas do dataframe
print(f"Total de linhas do dataframe: {df.count()}")

# Quantidade de nome
qtd_NOME = df.groupBy("ano", "sexo").count().orderBy(F.col("ano").desc())
qtd_NOME.show()

nome_fem_top = df.filter(df.sexo=="F")\
                    .groupBy("NOME", "ano")\
                    .agg(F.sum("total").cast("int").alias("total_registros"))\
                    .orderBy(F.col("total_registros").desc())\
                    .limit(1)
nome_fem_top.show()

nome_masc_top = df.filter(df.sexo=="M")\
                    .groupBy("NOME", "ano")\
                    .agg(F.sum("total").cast("int").alias("total_registros"))\
                    .orderBy(F.col("total_registros").desc())\
                    .limit(1)
nome_masc_top.show()

qtd_nome_por_genero = df.groupBy("sexo", "ano")\
                    .agg(F.sum("total").cast("int").alias("total_registros_por_genero"))\
                    .orderBy(F.col("ano").asc())\
                    .limit(10)
qtd_nome_por_genero.show()

dynamic_frame_para_salvar = DynamicFrame.fromDF(df, glueContext, "dynamic_frame_para_salvar")

glueContext.write_dynamic_frame.from_options(
    frame = dynamic_frame_para_salvar,
    connection_type = "s3",
    connection_options = {"path": target_path, "partitionKeys": ["sexo", "ano"]},
    format = "json"
)

job.commit()