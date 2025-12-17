SELECT cod, titulo, autor, editora, valor, publicacao, edicao, idioma
FROM livro
WHERE livro.publicacao > '2014-12-31'
ORDER BY livro.cod ASC