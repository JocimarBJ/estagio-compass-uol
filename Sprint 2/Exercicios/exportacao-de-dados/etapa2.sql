SELECT
	edi.codEditora  AS CodEditora,
	edi.nome        AS NomeEditora,
	COUNT(liv.cod)  AS QuantidadeLivros
FROM editora        AS edi
JOIN livro          AS liv ON liv.editora=edi.codeditora
GROUP BY edi.codEditora, edi.nome 
ORDER BY QuantidadeLivros DESC
LIMIT 5