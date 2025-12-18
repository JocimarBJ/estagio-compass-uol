SELECT 
    vend.nmvdd AS vendedor,
    SUM(venda.qtd * venda.vrunt) AS valor_total_vendas,
    ROUND(SUM(venda.qtd * venda.vrunt) * (vend.perccomissao /100.0), 2) AS comissao
FROM tbvendedor AS vend
JOIN tbvendas AS venda
    ON venda.cdvdd = vend.cdvdd
WHERE LOWER(venda.status) LIKE 'conclu%'
GROUP BY vend.cdvdd, vend.nmvdd, vend.perccomissao
ORDER BY comissao DESC;
