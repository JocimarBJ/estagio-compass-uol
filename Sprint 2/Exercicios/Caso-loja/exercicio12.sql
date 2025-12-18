WITH vendas_por_vendedor AS (
    SELECT
        cdvdd,
        SUM(qtd * vrunt) AS valor_total_vendas
    FROM tbvendas
    WHERE LOWER(status) LIKE 'conclu%'
    GROUP BY cdvdd
)
SELECT cddep, nmdep, dtnasc, val.valor_total_vendas
FROM tbdependente AS dep
JOIN vendas_por_vendedor AS val
    ON dep.cdvdd = val.cdvdd
WHERE val.valor_total_vendas=(
            SELECT MIN(valor_total_vendas)
            FROM vendas_por_vendedor
            WHERE valor_total_vendas > 0
            )
