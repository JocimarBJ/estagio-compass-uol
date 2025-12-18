SELECT estado, ROUND(AVG(qtd*vrunt),2) AS gastomedio
FROM tbvendas AS venda
WHERE LOWER(status) LIKE 'conclu%'
GROUP BY estado
ORDER BY gastomedio DESC
