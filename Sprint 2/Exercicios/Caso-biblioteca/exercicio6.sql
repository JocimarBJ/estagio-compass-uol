SELECT
    aut.codautor,
    aut.nome,
    count(liv.cod) AS quantidade_publicacoes
FROM autor aut
JOIN livro liv
    ON liv.autor = aut.codautor
GROUP BY
    aut.codautor,
    aut.nome
HAVING COUNT(liv.cod) = (
    SELECT MAX(qtd)
    FROM (
        SELECT COUNT(*) AS qtd
        FROM livro
        GROUP BY autor
    )
);