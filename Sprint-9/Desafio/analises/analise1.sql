-- Consistencia das Avaliações entre Gêneros
SELECT
    t.genero AS genero,
    ROUND(AVG(f.nota_media),2) AS media_nota,
    ROUND(STDDEV(f.nota_media),4) AS desvio_padrao,
    COUNT(DISTINCT f.sk_obra) AS qtd_obras
FROM fato_avaliacao f
JOIN dim_obra o 
    ON f.sk_obra = o.sk_obra

LATERAL VIEW explode(split(o.genero, ',')) t AS genero

WHERE t.genero IN ('comedy', 'animation')
GROUP BY t.genero
ORDER BY desvio_padrao ASC