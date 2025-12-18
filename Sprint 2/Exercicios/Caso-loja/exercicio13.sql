SELECT venda.cdpro, venda.nmcanalvendas, venda.nmpro, 
      SUM(venda.qtd) AS quantidade_vendas
FROM tbvendas AS venda
WHERE LOWER(venda.nmcanalvendas) IN ('ecommerce','matriz') 
      AND LOWER(venda.status) LIKE 'conclu%'
GROUP BY venda.cdpro, venda.nmcanalvendas, venda.nmpro
ORDER BY quantidade_vendas ASC
LIMIT 10