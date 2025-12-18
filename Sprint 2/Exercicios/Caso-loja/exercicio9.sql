SELECT venda.cdpro, venda.nmpro
FROM tbvendas AS venda
WHERE venda.dtven BETWEEN '2014-02-03' AND '2018-02-02'
  AND LOWER(REPLACE(venda.status, 'í', 'i')) = 'concluido'
GROUP BY venda.cdpro, venda.nmpro
HAVING SUM(venda.qtd) = (
    SELECT MAX(total)
    FROM (
        SELECT SUM(qtd) AS total
        FROM tbvendas
        WHERE dtven BETWEEN '2014-02-03' AND '2018-02-02'
          AND LOWER(REPLACE(status, 'í', 'i')) = 'concluido'
        GROUP BY cdpro
    )
)