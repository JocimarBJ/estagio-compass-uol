SELECT vend.cdvdd, vend.nmvdd
FROM tbvendedor AS vend
JOIN tbvendas AS venda
    ON venda.cdvdd = vend.cdvdd
GROUP BY vend.cdvdd, vend.nmvdd
HAVING COUNT(venda.cdven) = (
    SELECT MAX(qtd)
    FROM (
        SELECT COUNT(*) AS qtd
        FROM tbvendas
        GROUP BY cdvdd
    )
)
