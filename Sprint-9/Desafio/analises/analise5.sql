-- Influencia das Franquias na consistência
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