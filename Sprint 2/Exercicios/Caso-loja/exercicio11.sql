WITH gasto_por_cliente AS (
    SELECT 
        cdcli,
        nmcli,
        SUM(qtd * vrunt) AS gasto
    FROM tbvendas
    WHERE LOWER(status) LIKE 'conclu%'
    GROUP BY cdcli, nmcli
)
SELECT 
    cdcli,
    nmcli,
    gasto
FROM gasto_por_cliente
WHERE gasto = (
    SELECT MAX(gasto)
    FROM gasto_por_cliente
)
