-- Análise de Variabilidade Inter-gêneros e Formatos
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