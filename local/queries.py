from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import logging

spark = SparkSession.builder.appName("Queries").getOrCreate()

df_fato_avaliacao = spark.read.parquet("./3-refined/fato_avaliacao")
df_dim_obra = spark.read.parquet("./3-refined/dim_obra")
df_dim_franquia = spark.read.parquet("./3-refined/dim_franquia")
df_dim_tempo = spark.read.parquet("./3-refined/dim_tempo")

df_fato_avaliacao.createOrReplaceTempView("fato_avaliacao")
df_dim_obra.createOrReplaceTempView("dim_obra")
df_dim_franquia.createOrReplaceTempView("dim_franquia")
df_dim_tempo.createOrReplaceTempView("dim_tempo")

# 1. Silencia o log do Python
logging.getLogger("py4j").setLevel(logging.ERROR)

# 2. Silencia o log do Java/Spark
spark.sparkContext.setLogLevel("ERROR")

consistencia_avaliacoes_generos = spark.sql(
    """
    SELECT
        TRIM(t.genero) AS genero,
        ROUND(AVG(f.nota_media),2) AS media_nota,
        ROUND(STDDEV(f.nota_media),4) AS desvio_padrao,
        COUNT(DISTINCT f.sk_obra) AS qtd_obras
    FROM fato_avaliacao f
    JOIN dim_obra o 
        ON f.sk_obra = o.sk_obra

    LATERAL VIEW explode(split(o.genero, ',')) t AS genero

    WHERE TRIM(t.genero) IN ('comedy', 'animation')
    GROUP BY TRIM(t.genero)
    ORDER BY desvio_padrao ASC
    """
)
consistencia_avaliacoes_generos.show(10)

# Influência do formato (filme/série) na consistência
influencia_formato_consistencia = spark.sql(
    """
    SELECT
        o.tipo,
        ROUND(AVG(f.nota_media),2) AS media_nota,
        ROUND(STDDEV(f.nota_media),4) AS desvio_padrao,
        COUNT(f.sk_obra) AS qtd_obras
    FROM fato_avaliacao f
    JOIN dim_obra o 
        ON f.sk_obra = o.sk_obra
    GROUP BY o.tipo
    ORDER BY desvio_padrao ASC;
    """
)
influencia_formato_consistencia.show(10)

# Influência do engajamento na estabilidade das avaliações
influencia_engajamento_estabilidade_avaliacoes = spark.sql(
    """
    SELECT
        CASE 
            WHEN f.numero_votos < 2000 THEN 'baixo'
            WHEN f.numero_votos BETWEEN 2000 AND 10000 THEN 'medio'
            ELSE 'alto'
        END AS faixa_engajamento,
        ROUND(AVG(f.numero_votos),2) AS media_votos,
        ROUND(AVG(f.nota_media),2) AS media_nota,
        ROUND(STDDEV(f.nota_media),4) AS desvio_padrao,
        COUNT(sk_obra) AS qtd_obras

    FROM fato_avaliacao f
    GROUP BY faixa_engajamento
    ORDER BY desvio_padrao ASC;
    """
)
influencia_engajamento_estabilidade_avaliacoes.show(10)

# Impacto da popularidade na dispersão das notas
impacto_popularidade_dispersao_notas = spark.sql(
    """
    SELECT
        CASE 
            WHEN f.popularidade < 10 THEN 'baixa'
            WHEN f.popularidade BETWEEN 10 AND 30 THEN 'media'
            ELSE 'alta'
        END AS faixa_popularidade,
        ROUND(AVG(f.popularidade),2) AS media_popularidade,
        ROUND(AVG(f.nota_media), 2) AS media_nota,
        ROUND(STDDEV(f.nota_media),4) AS desvio_padrao,
        COUNT(f.sk_obra) AS qtd_obras

    FROM fato_avaliacao f
    JOIN dim_obra o 
        ON f.sk_obra = o.sk_obra
    GROUP BY faixa_popularidade
    ORDER BY desvio_padrao ASC;
    """
)
impacto_popularidade_dispersao_notas.show(10)

# Influência de franquias na consistência
influencia_franquias_consistencia = spark.sql(
    """
    SELECT
        fr.nome_franquia,
        ROUND(AVG(f.nota_media),2) AS media_nota,
        ROUND(STDDEV(f.nota_media),4) AS desvio_padrao,
        COUNT(f.sk_obra) AS qtd_obras
    FROM fato_avaliacao f
    JOIN dim_franquia fr 
        ON f.sk_franquia = fr.sk_franquia
    GROUP BY fr.nome_franquia
    HAVING COUNT(*) >= 2
    ORDER BY desvio_padrao ASC;
    """
)
influencia_franquias_consistencia.show(10)

# Cruzamento de Tipo (Série/Filme) com Gênero (Animação/Comédia)
analise_intergeneros_formatos = spark.sql(
    """
    SELECT 
        o.tipo, 
        t.genero, 
        ROUND(AVG(f.nota_media), 2) AS media_nota, 
        ROUND(STDDEV(f.nota_media), 4) AS desvio_padrao, 
        COUNT(f.sk_obra) AS qtd_obras
    FROM fato_avaliacao f 
    JOIN dim_obra o
        ON f.sk_obra = o.sk_obra

    LATERAL VIEW explode(split(o.genero, ',')) t AS genero

    WHERE t.genero IN ('animation', 'comedy')
    GROUP BY o.tipo, t.genero
    ORDER BY o.tipo DESC, media_nota DESC
    """
)
analise_intergeneros_formatos.show()