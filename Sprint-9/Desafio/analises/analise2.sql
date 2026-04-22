-- Influência do formato (filme/serie) na consistencia
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