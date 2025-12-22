SELECT
      liv.cod         AS CodLivro,
      liv.titulo      AS Titulo,
      aut.codAutor    AS CodAutor,
      aut.nome        AS NomeAutor,
      liv.valor       AS Valor,
      edi.codEditora  AS CodEditora,
      edi.nome        AS NomeEditora
FROM  livro           AS liv
INNER JOIN editora    AS edi ON edi.codEditora = liv.editora
INNER JOIN autor      AS aut ON aut.codAutor = liv.autor
ORDER BY liv.valor    DESC
LIMIT 10