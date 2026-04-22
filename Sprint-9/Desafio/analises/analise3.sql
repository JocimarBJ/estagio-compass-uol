-- Influencia do engajamento na estabilidade das avaliações
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