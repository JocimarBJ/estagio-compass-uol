SELECT DISTINCT
    aut.nome
FROM autor AS aut
LEFT JOIN livro AS liv
    ON liv.autor = aut.codAutor
LEFT JOIN editora AS edi
    ON edi.codEditora = liv.editora
LEFT JOIN endereco as en
    ON en.codEndereco = edi.endereco
WHERE en.estado NOT in ('RIO GRANDE DO SUL', 'SANTA CATARINA', 'PARANÁ')
ORDER BY aut.nome ASC