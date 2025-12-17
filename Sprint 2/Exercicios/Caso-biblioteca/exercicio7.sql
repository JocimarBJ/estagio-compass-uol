SELECT aut.nome
FROM autor as aut
LEFT JOIN livro as liv
    ON liv.autor = aut.codAutor
WHERE liv.cod IS NULL
ORDER BY aut.nome ASC