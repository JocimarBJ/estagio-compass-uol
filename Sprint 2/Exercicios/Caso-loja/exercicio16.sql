SELECT estado, nmpro, ROUND(AVG(qtd),4) AS quantidade_media
FROM tbvendas AS venda
WHERE LOWER(status) LIKE 'conclu%'
GROUP BY estado, nmpro
ORDER BY estado, nmpro
