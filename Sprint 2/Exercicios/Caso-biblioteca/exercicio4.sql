SELECT
    nome, codautor,nascimento,
    (SELECT count(*)
     FROM livro
     WHERE autor = codautor) AS quantidade
FROM autor
ORDER BY REPLACE(nome, 'Á', 'A');