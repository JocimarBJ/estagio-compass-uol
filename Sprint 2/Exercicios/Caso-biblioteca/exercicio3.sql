SELECT count(liv.cod) as quantidade, edi.nome, en.estado, en.cidade
FROM livro AS liv
LEFT JOIN editora AS edi
    ON edi.codEditora = liv.editora
LEFT JOIN endereco AS en
    ON en.codEndereco = edi.endereco
GROUP BY edi.codEditora, edi.nome, en.estado, en.cidade
ORDER BY quantidade DESC
LIMIT 5