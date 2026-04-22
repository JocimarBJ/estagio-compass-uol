-- Impacto da popularidade na dispersão das notas
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