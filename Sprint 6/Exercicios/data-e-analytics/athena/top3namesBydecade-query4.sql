WITH ranking AS (
    SELECT
        FLOOR(ano/10)*10 AS decada,
        nome,
        SUM(total) AS total,
        DENSE_RANK() OVER(
            PARTITION BY FLOOR(ano/10)*10
            ORDER BY SUM(total) DESC
        ) AS posicao
        FROM meubanco.dados_pessoas
        WHERE ano >= 1950
        GROUP BY FLOOR(ano/10)*10, nome
)
SELECT decada, nome, total
FROM ranking
WHERE posicao <= 3
ORDER BY decada, total DESC;
