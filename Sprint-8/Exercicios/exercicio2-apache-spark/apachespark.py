
# =================== ETAPA 1 ====================
print("=========== ETAPA 1 ===========")
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

spark = SparkSession \
        .builder \
        .master ("local[*]") \
        .appName("Exercicio2 Etapa1") \
        .getOrCreate()

df_nomes = spark.read.csv("Sprint-8/Exercicios/exercicio1-geracao-e-massas/etapa-3/nomes_aleatorios.txt")
df_nomes.show(5)

# =================== ETAPA 2 ====================
print("=========== ETAPA 2 ===========")
print("Renomear coluna para 'Nomes'")
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.printSchema()
df_nomes.show(10)

# =================== ETAPA 3 ====================
print("=========== ETAPA 3 ===========")
print("Coluna Escolaridade adicionada")
from pyspark.sql.functions import rand, when
df_nomes = df_nomes.withColumn("Escolaridade",
                               when( (rand() < 0.33), "Fundamental")
                               .when( (rand() < 0.66), "Medio")
                               .otherwise("Superior")           
                               )

# =================== ETAPA 4 ====================
print("=========== ETAPA 4 ===========")
print("Coluna País adicionada")
from pyspark.sql.functions import floor
paises = [
    "Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador",
    "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"
]

df_nomes = df_nomes.withColumn(
    "Pais",
    when( floor(rand()*13) == 0, paises[0]    )
    .when( floor(rand()*13) == 1, paises[1]   )
    .when( floor(rand()*13) == 2, paises[2]   )
    .when( floor(rand()*13) == 3, paises[3]   )
    .when( floor(rand()*13) == 4, paises[4]   )
    .when( floor(rand()*13) == 5, paises[5]   )
    .when( floor(rand()*13) == 6, paises[6]   )
    .when( floor(rand()*13) == 7, paises[7]   )
    .when( floor(rand()*13) == 8, paises[8]   )
    .when( floor(rand()*13) == 9, paises[9]   )
    .when( floor(rand()*13) == 10, paises[10] )
    .when( floor(rand()*13) == 11, paises[11] )
    .otherwise(paises[12])
)

# =================== ETAPA 5 ====================
print("=========== ETAPA 5 ===========")
print("Filtrar pessoas de 1945 à 2010")
df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    (floor(rand() * (2010 - 1945 + 1)) + 1945) 
)

df_nomes.show(10)

# =================== ETAPA 6 ====================
print("=========== ETAPA 6 ===========")
print("Filtrar pessoas do século 21")
from pyspark.sql.functions import col

df_select = df_nomes.select("*").filter(col("AnoNascimento") >= 2001)

df_select.show(10)

# =================== ETAPA 7 ====================
print("=========== ETAPA 7 ===========")
print("Filtrar pessoas do século 21 (versão SQL)")
from pyspark.sql.functions import col

df_nomes.createOrReplaceTempView("pessoas")
spark.sql("""
          SELECT * 
          FROM pessoas 
          WHERE pessoas.AnoNascimento >= 2001
          """
          ).show(10)

# =================== ETAPA 8 ====================
print("=========== ETAPA 8 ===========")
print("Filtrar Millennials")
df_millennials = df_nomes.filter( col("AnoNascimento").between(1980, 1994) )
df_millenials = df_millennials.count()
print(f"Numero de pessoas millenials: {df_millenials}")

# =================== ETAPA 9 ====================
print("=========== ETAPA 9 ===========")
print("Filtrar Millennial (versão SQL)")
spark.sql(
        """
        SELECT COUNT(*) AS qtd_millennials
        FROM pessoas
        WHERE AnoNascimento BETWEEN 1980 AND 1994
        """
        ).show()

# =================== ETAPA 10 ====================
print("=========== ETAPA 10 ===========")
print("Classificar por geração")
spark.sql(
        """
        SELECT Pais,
        CASE
                WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
                WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
                WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
                WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
        END AS Geracao,
        COUNT(*) AS Quantidade
        FROM pessoas
        GROUP BY Pais, Geracao
        ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
        """
        ).show(truncate=False)