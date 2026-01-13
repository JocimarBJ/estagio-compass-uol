# 📝 Resumo
 
|<h3>🔍ÍNDICE</h3>|
|------------------|
| [🧠 Competências Aplicadas](#-competências-aplicadas) |
| [👨‍💻 Curso 1 - SQL para Análise de Dados](#%E2%80%8D-curso-sql-para-análise-de-dados---do-básico-ao-avançado) |
| [📊 Curso 2 - Data & Analytics](#-curso-data--analytics---pb---aws-210)                           |
| [✍ Exercícios](#-exercícios) |
| [👁‍🗨 Evidências](#%E2%80%8D-evidências) |
| [🎯 Desafio da Sprint](#-desafio-da-sprint)  |
| [✅ Certificados](#-certificados) |


## 🧠 Competências aplicadas
- SQL avançado
- Tratamento e exportação de dados
- Modelagem e raciocínio relacional
- Análise de dados
- Boas práticas de legibilidade

## 👨‍💻 Curso: SQL Para Análise de Dados - Do Básico ao Avançado
### 🔧 Seção 2: Configuração do ambiente de trabalho
Como meu pgAdmin já estava instalado na minha máquina, eu somente fiz a revisão do que foi passado para ver se não havia ausência de algum fator fundamental para a execução dos futuros exercícios;

### ⌨️ Seção 3: Comandos básicos
A maioria dos comandos, como Select, Where, Order By eu já conhecia, no entanto pude aprender como funcionava o Limit e o Distinct.
- Podemos utilizar o asterisco `*` quando desejamos printar todas as colunas da tabela e seus dados.
- `SELECT` usamos frequentemente na linguagem SQL, serve para selecionarmos colunas de tabelas e mostrar os dados filtrados.
  <details><summary>Exemplo:</summary>

  `SELECT usernames FROM game.users`</details>

- `WHERE` é utilizado em conjunto com o Select e serve para filtrar as linhas da tabela de acordo com a condição que você impõe.
  <details><summary>Exemplo:</summary>
  
  `SELECT email, state FROM sales.customers WHERE state = 'SC'`.<br>
  Dessa forma, somente àqueles que corresponderem com a sigla SC será mostrado.</details>
- `DISTINCT` serve para remover linhas duplicadas, mostrando apenas as linhas que distinguem, evitando que informações se repitam. Utilizado logo após o SELECT. 
  <details><summary>Exemplo:</summary>
  
  `SELECT DISTINCT brand FROM sales.products`.</details>
- `ORDER BY` serve para ordenar de acordo com a regra definida, por exemplo decrescente, crescente e etc.
- `LIMIT` é utilizado para limitar o número de linhas da consulta. Utilizado sempre no final da linha.

Houve demais informações e detalhes durante as aulas, como: não utilizar vírgula antes do FROM e etc. Algo que observei não ser retratado foi que uma boa prática para comandos SQL é utilizar eles em maiúsculo, por exemplo: `SELECT email FROM ...` ao invés de `Select Email FROM ...`, visando a organização e formatação textual, como uma melhor compreensão e praticidade para qualquer desenvolvedor que estiver lendo.

### ➗ Seção 4: Operadores
Temos diversos tipos de operadores, sendo eles **aritméticos, comparação e lógicos**.
Eles servem para executarmos cálculos matemáticos, comparar valores retornando *true* ou *false* e unir expressões simples em uma composta. <br>
São muitos, mas podemos citar alguns como, respectivamente:
- ``` ||, +, -, *, /, ^, %...```
- ``` =, <=, =>, <>, >, <...```
- ``` AND, OR, NOT, IN, ON, LIKE, USING... ```

### 🔁 Seção 5: Funções Agregadas
Existem vários tipos de funções agregadas, sendo elas: Count(), Sum(), Min(), Max(), Avg(), Group By e Having.
- `COUNT( )` serve para contabilizar
- `SUM( )` serve para somar
- `MIN( )` pega o menor/calcula o mínimo
- `MAX( )` pega o máximo/calcula o máximo
- `AVG( )` calcula a média
- `GROUP BY`: serve para agrupar os registros semelhantes da coluna. Se usado somente ele, funciona como o DISTINCT
- `HAVING`: serve para filtrar as linhas de seleção por uma coluna já agregadas. Diferente do WHERE que só pode filtrar colunas não agregadas, a função HAVING pode filtrar tanto colunas agregadas como não agregadas.

As funções agregadas não computam células NULL como zero, elas ignoram.

### ⚙️ Seção 6: Join
Existem 4 tipos de Join para serem utilizados no SQL, sendo eles:
- ⟗ `FULL JOIN` pega todos os dados, tanto da tabela da esquerda (tabela declarada primeiro) e tabela da direita (tabela declarada depois).
- ⟕ `LEFT JOIN` pega todos os dados da tabela da esquerda, e da tabela da direita pega somente aqueles correspondentes à tabela da esquerda.
- ⨝ `INNER JOIN` pega a intersecção de dados entre a tabela Left e a tabela Right.
- ⟖ `RIGHT JOIN` pega todos os dados da tabela da direita, mesma coisa do Left Join, porém o contrário.

São mais comumente utilizados o Left Join e o Inner Join. Além disso, baseando-se nesses 4 comandos de Join, podemos conseguir uma variação de até 8 jeitos diferentes de extrair os dados na consulta, como:
`USING, NATURAL JOIN, SELF JOIN, CROSS JOIN, OUTER JOIN`

### <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Venn_0111_1111.svg/250px-Venn_0111_1111.svg.png" width="18" style="vertical-align: middle"/> Seção 7: Unions
O comando ``UNION`` serve basicamente para unir uma tabela sobre a outra, desde que tenham a mesma quantidade de colunas e essas colunas sejam do mesmo tipo.
Existe o `UNION ALL` e o `UNION`, sendo sua principal diferença que o UNION ALL não checa e remove as linhas duplicadas.

*É recomendado utilizar somente o UNION ALL quando sabemos que o conteúdo das tabelas são diferentes.*

### 🔀 Seção 8: Subqueries
As Subqueries servem para que possamos consultar os dados de outras consultas que estão embutidas, ou seja, utilizar os resultados de uma query dentro de outra query.
Existem 4 tipos de Subquery, basicamente são no: `WHERE, WITH, FROM e SELECT`.

Alguns pontos de atenção seriam:
- Sempre ao utilizar no WHERE, a Subquery deve retornar apenas um valor, não mais que uma linha ou coluna.
- Subqueries com WITH é muito mais legível e cria como se fosse uma "tabela fantasma"
- Não é recomendado utilizar Subquery no FROM, já que toda subquery no FROM pode ser substituída por uma com WITH
- A Subquery no SELECT é bem pesada, é como se estivesse rodando uma query a cada linha. Algumas vezes é o único jeito de responder uma pergunta, mas é bom evitar usar. Além disso, ela só pode retornar um dado, como no caso do WHERE.

### 🔄 Seção 9: Tratamento de Dados

- **Conversão de Unidades**: <br>
  Existem dois jeitos de conversão (type casting), uma das formas utiliza `::` e na outra a função `CAST()`, basicamente. Existem outras funções, que serão citadas mais a abaixo.
  - Para utilizar o `::`, devemos seguir o seguinte padrão `dado_da_tabela::formato_pretendido`. Exemplo: `112233::text`.
    <details><summary>Exemplo:</summary>

    Para utilizar o Cast( ), devemos:
      ```SQL
      CAST(dado_seu AS formato_pretendido)
      --Exemplo: SELECT CAST(20050124 AS DATE)
      ```
    </details>

- **Tratamento Geral**:<br>
  Nesta parte utilizamos dois tipos, sendo eles CASE WHEN e COALESCE( )
  - `CASE WHEN` é usado para agrupamento de dados. No primeiro When a condição deve ser verdadeira e qual resultado esperamos caso ela seja verdadeira. A lógica é bem parecida com SWITCH CASE nas linguagens de programação. No CASE WHEN nós utilizamos os operadores lógicos e deve sempre ser finalizado com END.
  - `COALESCE( )` é usado para tratamento de dados nulos. Dentro do COALESCE pode-se colocar uma sequência de valores separados por vírgula. Primeiro, ele verifica qual é o primeiro campo não nulo de uma lista de valores e vai retornando valor por valor que não seja nulo, todos que ele considerar nulo ele vai ignorar e trocando os valores nulos pelo primeiro não nulo dentro do parênteses. 
    <details>
    <summary>
    Exemplo:
    </summary>

      ```SQL
      SELECT nome,
      COALESCE(email, telefone, 'Sem contato') AS contato
      FROM clientes;

      Se email existir → usa email
      senão, se telefone existir → usa telefone
      senão → 'Sem Contato'
      ```
      → Transformando isso:
      |nome|email|telefone|
      |:-:|:-:|:-:|
      |Joao|joao@gmail.com|999-111|
      |Ana|Null|888-222|
      |Carlos|Null|Null|
      
      → Nisso:
      |nome|contato|
      |:-:|:-:|
      |Joao|joao@gmail.com|
      |Ana|888-222|
      |Carlos|Sem Contato|
    </details>
- **Tratamento de Texto**:<br>
LOWER( ), UPPER( ), TRIM( ), REPLACE( ) são algumas das formas de tratamento de texto apresentadas.
  - `LOWER()` basicamente deixa toda a string em minúsculo
  - `UPPER()` deixa toda a string em maiúsculo
  - `TRIM()` retira os espaços em brancos das extremidades de uma string
  - `REPLACE()` substitui a parte da string passada no parâmetro, juntamente com o que queremos colocar no lugar.
    <details>
    <summary>
    Exemplo:
    </summary>

      ```SQL
      REPLACE('SAO PAULO', 'SAO', 'SÃO') = 'SÃO PAULO'
      -- irá retornar TRUE
      ```
    </details>
<br>

- **Tratamento de Datas**:<br>
Existem 4 funções muito utilizadas para tratar datas e horas, sendo elas:
  - `INTERVAL()` serve para definir um intervalo específico de tempo, por exemplo, quando você quer somar semanas, meses, horas, anos e etc, ao invés de apenas dias (default).
  - `DATE_TRUNC()` trunca as datas, por exemplo, caso queira que "corte" por mês, por ano e etc.
  - `EXTRACT()` serve para extrair as unidades de uma data, ou seja, se você quer saber qual dia da semana aquela data se refere, você pode utilizar o extract( ), onde ele retornará um número representativo.
  - `DATEDIFF()` calcula a diferença entre datas, mas diferente de apenas utilizar o operador de subtração, utilizar o datediff( ) nos dá a possibilidade e maior clareza de especificar qual diferença queremos que retorne informando o período, por exemplo, a diferença de semanas, meses, anos e etc, só de utilizar strings como *weeks*, *months* e *years*.

- **Funções**:<br>
As funções servem para criarmos comandos personalizados de scripts que serão usados comumente. No entanto, devido à sua complexidade de criação não é algo que usamos com muita frequência, mas quando precisamos é sempre mais prático.

  Para criarmos uma função, precisamos de algumas coisas antes:
  - Definir que tipo de função será e para qual finalidade
  - Criar o escopo da consulta para ter certeza do caminho que irá seguir
  - Definir um nome para ela que torne claro a sua funcionalidade e não traga ambiguidade
  - Definir quais serão as variáveis de entrada passadas por parâmetro e as variáveis de saída

  <details>
  <summary>
  Exemplo Prático:
  </summary>

    ```SQL
    --Escopo
    select datediff('weeks', '2018-06-01', current_date)

    --Função 
    --Modelo: 
      -- nome_da_função(variavel1 tipo1, variavel2 tipo2...) 
      -- RETURNS tipo_da_saida 
      -- LANGUAGE linguagem_selecionada
      -- AS $$ script_query $$

    CREATE FUNCTION datediff(unidade varchar, data_inicial date, data_final date)
    RETURNS integer
    LANGUAGE SQL
    AS $$
      SELECT CASE
        WHEN unidade IN ('d', 'day', 'days') THEN (data_final - data_inicial)
        WHEN unidade IN ('w', 'week', 'weeks') THEN (data_final - data_inicial)/7
        WHEN unidade IN ('m', 'month', 'months') then (data_final - data_inicial)/30
        WHEN unidade IN ('y', 'year', 'years') THEN (data_final - data_inicial)/365
        END AS diferenca
    $$

    --Deletar Função
    DROP FUNCTION nome_da_funcao
    ```
  </details>

### 🔣 Seção 10: Manipulação de Tabelas:
- **Tabelas - Criação e Deleção:**
  <details>
  <summary>
  Existem 2 formas de criar uma tabela:
  </summary>

  - A partir de uma Query: Após fazer a query, utilizamos o comando `INTO` + nome_que_queremos antes do FROM. Após isso, ao invés de sempre termos que fazer uma query para obter o mesmo resultado, podemos simplesmente invocar a tabela com o nome que colocamos.
  - A partir do Zero: Usamos o comando `CREATE TABLE nome_que_queremos(variavel1 tipo 1, variavel2 tipo2,...)`. No entanto, a tabela estará vazia, então para preenchê-la usamos:
    ```SQL
    INSERT INTO nome_que_colocamos(parâmetro1, parâmetro2,...)
    VALUES(valor1, valor1_modificado)(valor2, valor2_modificado...)
    ```
  - Para excluir a tabela usamos `DROP TABLE nome_que_usamos`

<br>

- **Linhas - Inserção, Atualização e Deleção:**
  <details>
  <summary>
  Para inserir linhas, a sintaxe é parecida, utilizamos:
  </summary>

    ```SQL
    INSERT INTO nome_da_tabela(parametro1, parametro2) VALUES (valor1, valor1_modificado...)
    ```
  </details>

  <details>
  <summary>
  Para atualizar alguma informação de uma linha, usamos:
  </summary>

    ```SQL
    UPDATE nome_da_tabela
    SET coluna = dado_modificado 
    WHERE coluna2 = dado_correspondente
    ```
  </details>

  <details>
  <summary>
  Para deletar, usamos:
  </summary>

    ```SQL
    DELETE FROM nome_da_tabela
    WHERE coluna1 = dado_correspondente
    ```
  </details>
<br>

- **Colunas - Inserção, Atualização e Deleção:**<br>
  <details>
  <summary>
  Para inserirmos colunas em uma tabela, usamos:
  </summary>

    ```SQL
    ALTER TABLE nome_da_tabela
    ADD nome_da_coluna tipo_da_coluna
    ```
  </details>

  <details>
  <summary>
  Para atualizarmos/inserirmos dados de uma coluna:
  </summary>
  
    ```SQL
    UPDATE nome_da_tabela
    SET nome_da_coluna = dado_que_voce_quer
    WHERE true 
    --true serve para quando queremos que todas as linhas sejam atualizadas.
    ```
    </details>

    <details>
    <summary>
    Se quisermos por exemplo atualizar o tipo da coluna ou renomeá-la:
    </summary>

    ```SQL
    --Alterar tipo
    ALTER TABLE nome_da_tabela
    ALTER COLUMN nome_da_coluna type tipo

    --Renomear
    ALTER TABLE nome_da_tabela
    RENAME COLUMN nome_da_coluna TO novo_nome
    ```
    </details>

  Para deletar uma coluna, usamos: `ALTER TABLE nome_da_tabela DROP COLUMN nome_da_coluna`

### 📒 Seção 11: Projeto 1 - Dashboard de Acompanhamento de Vendas
Para a criação do Dashboard, no Excel precisamos definir 3 páginas, sendo elas a janela do Dashboard que puxará os dados da janela dos Resultados e por fim uma janela para documentar as Queries.
Durante a realização do projeto utilizamos todos os conhecimentos adquiridos ao longo do curso para formar um dashboard representativo dos dados, trazendo-os de forma mais visualmente clara.

### 📒 Seção 12: Projeto 2 - Análise de Perfil dos Clientes
No projeto 2 exemplar utilizamos dos mesmos conhecimentos para resolver o problema e representar como gráficos. Os gráficos, como no projeto 1, foram apresentados no Excel e foi dividido da mesma forma as suas páginas.

## 📊 Curso: Data & Analytics - PB - AWS 2/10
**Modelagem Relacional**: A modelagem relacional tem como principal objetivo organizar os dados de forma estruturada, consistente e sem redundâncias, garantindo a integridade das informações. Nessa abordagem, os dados são divididos em tabelas normalizadas, cada uma representando uma entidade específica, como clientes, vendedores ou produtos. As relações entre essas entidades são estabelecidas por meio de chaves primárias e estrangeiras, assegurando coerência referencial. A normalização reduz anomalias de inserção, atualização e exclusão, tornando o modelo mais confiável para sistemas transacionais. Esse tipo de modelagem é amplamente utilizado em bancos de dados OLTP, onde há grande volume de operações de leitura e escrita. Além disso, facilita a manutenção e evolução do sistema ao longo do tempo. A modelagem relacional serve como base sólida para posteriores transformações analíticas.

**Modelagem Dimensional**: A modelagem dimensional é voltada para análise de dados e tomada de decisão, priorizando desempenho e facilidade de consulta. Nela, os dados são organizados em tabelas fato e tabelas dimensão, sendo a tabela fato responsável por armazenar métricas quantitativas e as dimensões por fornecer contexto analítico. O modelo Star Schema, utilizado neste projeto, simplifica as consultas ao reduzir a quantidade de junções necessárias. Essa abordagem é amplamente aplicada em ambientes de Business Intelligence e Data Warehousing. Diferentemente do modelo relacional, a modelagem dimensional aceita certa redundância para otimizar consultas analíticas. Além disso, o uso de dimensões como tempo permite análises históricas detalhadas. Dessa forma, o modelo dimensional torna os dados mais acessíveis e eficientes para análises estratégicas.
# ✍ Exercícios

### 📚 Seção 10 - Caso de Estudo Biblioteca
1. <details><summary><a href="./Exercicios/Caso-biblioteca/exercicio1.sql">Resposta Ex1</a></summary>
    
    ```SQL
    SELECT cod, titulo, autor, editora, valor, publicacao, edicao, idioma
    FROM livro
    WHERE livro.publicacao > '2014-12-31'  
    ORDER BY livro.cod ASC
    ```
   </details>

2. <details><summary><a href="./Exercicios/Caso-biblioteca/exercicio2.sql">Resposta Ex2</a></summary>
    
    ```SQL
    SELECT titulo, valor
    FROM livro
    ORDER BY valor DESC
    LIMIT 10
    ```
   </details>

3. <details><summary><a href="./Exercicios/Caso-biblioteca/exercicio3.sql">Resposta Ex3</a></summary>
    
    ```SQL
    SELECT count(liv.cod) AS quantidade, 
           edi.nome, 
           en.estado, 
           en.cidade
    FROM livro            AS liv
    LEFT JOIN editora     AS edi ON edi.codEditora = liv.editora
    LEFT JOIN endereco    AS en  ON en.codEndereco = edi.endereco
    GROUP BY 
      edi.codEditora, 
      edi.nome, 
      en.estado, 
      en.cidade
    ORDER BY quantidade DESC
    LIMIT 5
    ```
   </details>

4. <details><summary><a href="./Exercicios/Caso-biblioteca/exercicio4.sql">Resposta Ex4</a></summary>
    
    ```SQL
    SELECT
    nome, codautor,nascimento,
      (SELECT count(*)
      FROM livro
      WHERE autor = codautor) AS quantidade
    FROM autor
    ORDER BY REPLACE(nome, 'Á', 'A');
    ```
   </details>

5. <details><summary><a href="./Exercicios/Caso-biblioteca/exercicio5.sql">Resposta Ex5</a></summary>

   > Também teria o mesmo resultado utilizando o INNER JOIN/JOIN
    
    ```SQL
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
    ```
   </details>

6. <details><summary><a href="./Exercicios/Caso-biblioteca/exercicio6.sql">Resposta Ex6</a></summary>
    
    ```SQL
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
    HAVING count(liv.cod) = (
        SELECT MAX(qtd)
        FROM (
            SELECT count(*) AS qtd
            FROM livro
            GROUP BY autor
        )
    )
    ```
   </details>

7. <details><summary><a href="./Exercicios/Caso-biblioteca/exercicio7.sql">Resposta Ex7</a></summary>
    
    ```SQL
    SELECT aut.nome
    FROM autor as aut
    LEFT JOIN livro as liv
        ON liv.autor = aut.codAutor
    WHERE liv.cod IS NULL
    ORDER BY aut.nome ASC
    ```
   </details>

### 🛒 Seção 11 - Caso de Estudo Loja

8. <details><summary><a href="./Exercicios/Caso-loja/exercicio8.sql">Resposta Ex8</a></summary>
    
    ```SQL
    SELECT vend.cdvdd, vend.nmvdd
    FROM tbvendedor AS vend
    JOIN tbvendas AS venda
        ON venda.cdvdd = vend.cdvdd
    GROUP BY vend.cdvdd, vend.nmvdd
    HAVING COUNT(venda.cdven) = (
        SELECT MAX(qtd)
        FROM (
            SELECT COUNT(*) AS qtd
            FROM tbvendas
            GROUP BY cdvdd
        )
    )
    ```
   </details>

9. <details><summary><a href="./Exercicios/Caso-loja/exercicio9.sql">Resposta Ex9</a></summary>
    
    ```SQL
    SELECT venda.cdpro, venda.nmpro
    FROM tbvendas AS venda
    WHERE venda.dtven BETWEEN '2014-02-03' AND '2018-02-02'
      AND LOWER(REPLACE(venda.status, 'í', 'i')) = 'concluido'
    GROUP BY venda.cdpro, venda.nmpro
    HAVING SUM(venda.qtd) = (
        SELECT MAX(total)
        FROM (
            SELECT SUM(qtd) AS total
            FROM tbvendas
            WHERE dtven BETWEEN '2014-02-03' AND '2018-02-02'
              AND LOWER(REPLACE(status, 'í', 'i')) = 'concluido'
            GROUP BY cdpro
        )
    )
    ```
   </details>

10. <details><summary><a href="./Exercicios/Caso-loja/exercicio10.sql">Resposta Ex10</a></summary>
      
      ```SQL
      SELECT 
          vend.nmvdd AS vendedor,
          SUM(venda.qtd * venda.vrunt) AS valor_total_vendas,
          ROUND(SUM(venda.qtd * venda.vrunt) * (vend.perccomissao /100.0), 2) AS comissao
      FROM tbvendedor AS vend
      JOIN tbvendas AS venda
          ON venda.cdvdd = vend.cdvdd
      WHERE LOWER(venda.status) LIKE 'conclu%'
      GROUP BY vend.cdvdd, vend.nmvdd, vend.perccomissao
      ORDER BY comissao DESC;
      ```
    </details>

11. <details><summary><a href="./Exercicios/Caso-loja/exercicio11.sql">Resposta Ex11</a></summary>
      
      ```SQL
      WITH gasto_por_cliente AS (
          SELECT 
              cdcli,
              nmcli,
              SUM(qtd * vrunt) AS gasto
          FROM tbvendas
          WHERE LOWER(status) LIKE 'conclu%'
          GROUP BY cdcli, nmcli
      )
      SELECT 
          cdcli,
          nmcli,
          gasto
      FROM gasto_por_cliente
      WHERE gasto = (
          SELECT MAX(gasto)
          FROM gasto_por_cliente
      )
      ```
    </details>

12. <details><summary><a href="./Exercicios/Caso-loja/exercicio12.sql">Resposta Ex12</a></summary>
      
      ```SQL
      WITH vendas_por_vendedor AS (
          SELECT
              cdvdd,
              SUM(qtd * vrunt) AS valor_total_vendas
          FROM tbvendas
          WHERE LOWER(status) LIKE 'conclu%'
          GROUP BY cdvdd
      )
      SELECT cddep, nmdep, dtnasc, val.valor_total_vendas
      FROM tbdependente AS dep
      JOIN vendas_por_vendedor AS val
          ON dep.cdvdd = val.cdvdd
      WHERE val.valor_total_vendas=(
                  SELECT MIN(valor_total_vendas)
                  FROM vendas_por_vendedor
                  WHERE valor_total_vendas > 0
                  )

      ```
    </details>

13. <details><summary><a href="./Exercicios/Caso-loja/exercicio13.sql">Resposta Ex13</a></summary>
      
      ```SQL
      SELECT venda.cdpro, venda.nmcanalvendas, venda.nmpro, 
      SUM(venda.qtd) AS quantidade_vendas
      FROM tbvendas AS venda
      WHERE LOWER(venda.nmcanalvendas) IN ('ecommerce','matriz') 
            AND LOWER(venda.status) LIKE 'conclu%'
      GROUP BY venda.cdpro, venda.nmcanalvendas, venda.nmpro
      ORDER BY quantidade_vendas ASC
      LIMIT 10
      ```
    </details>

14. <details><summary><a href="./Exercicios/Caso-loja/exercicio14.sql">Resposta Ex14</a></summary>
      
      ```SQL
      SELECT estado, ROUND(AVG(qtd*vrunt),2) AS gastomedio
      FROM tbvendas AS venda
      WHERE LOWER(status) LIKE 'conclu%'
      GROUP BY estado
      ORDER BY gastomedio DESC
      ```
    </details>

15. <details><summary><a href="./Exercicios/Caso-loja/exercicio15.sql">Resposta Ex15</a></summary>
      
      ```SQL
      SELECT cdven
      FROM tbvendas AS venda
      WHERE venda.deletado = '1'
      ORDER BY cdven ASC
      ```
    </details>

16. <details><summary><a href="./Exercicios/Caso-loja/exercicio16.sql">Resposta Ex16</a></summary>
      
      ```SQL
      SELECT estado, nmpro, ROUND(AVG(qtd),4) AS quantidade_media
      FROM tbvendas AS venda
      WHERE LOWER(status) LIKE 'conclu%'
      GROUP BY estado, nmpro
      ORDER BY estado, nmpro
      ```
    </details>

### 📨 Seção 13 - Exportação de Dados
- <details><summary><a href="./Exercicios/Exportacao-de-dados/etapa1.sql">3.1 - Etapa 1</a></summary>

  - **Enunciado**:
  ![Enunciado Etapa 1](./Exercicios/Exportacao-de-dados/imagens-execucao/enunciado-etapa1.png)
  - **Resposta**:
    ```SQL
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
    ORDER BY liv.valor DESC
    LIMIT 10
    ```
  - **Resultado**:
    [Tabela - Etapa 1](./Exercicios/Exportacao-de-dados/etapa1-livros_mais_caros.csv)
    | CodLivro | Titulo| CodAutor | NomeAutor| Valor | CodEditora | NomeEditora |
    |:--------:|:-----:|:--------:|:--------:|:-----:|:----------:|:-----------:|
    | 13       | Princípios de fisiologia animal | 8  | ABRAMOVAY, Ricardo | 515.64 | 13 | CBMM |
    | 9        | Fundamentos de eletrônica | 46 | AMARAL, Luciano Do | 515.04 | 13 | CBMM |
    | 93       | O verão das rosas | 39 | ALVES, Rubem | 514.70 | 13 | CBMM |
    | 8        | Artesão de saberes | 47 | ASTOLFI, Jean-Pierre | 512.22 | 13 | CBMM |
    | 45       | O texto estranho | 72 | BARROS, Regina Mambeli | 511.84 | 13 | CBMM |
    | 28       | Limitaciones y usos del derecho de construir | 55 | BALTAR, Carlos Adolpho Magalhães | 496.59 | 13 | CBMM |
    | 162      | Agente penitenciário | 5  | ABE, Jair Minoro | 489.27 | 1  | Ática |
    | 161      | O casamento da Bruxa Onilda | 36 | ALVARENGA, Beatriz Gonçalves De | 480.81 | 1  | Ática |
    | 168      | Direito social na União Européia e Mercosul | 45 | AMARAL, Adriano Benayon Do | 480.80 | 1  | Ática |
    | 19       | Machinapolis e a caosmologia do ser | 31 | ALMEIDA, Rogério Henrique | 479.90 | 13 | CBMM |
  </details>


- <details><summary><a href="./Exercicios/Exportacao-de-dados/etapa1.sql">3.2 - Etapa 2</a></summary>

  - **Enunciado**:

    ![Enunciado Etapa 1](./Exercicios/Exportacao-de-dados/imagens-execucao/enunciado-etapa2.png)

  - **Resposta**:
    ```SQL
    SELECT
      edi.codEditora  AS CodEditora,
      edi.nome        AS NomeEditora,
      COUNT(liv.cod)  AS QuantidadeLivros
    FROM editora        AS edi
    JOIN livro          AS liv ON liv.editora=edi.codeditora
    GROUP BY edi.codEditora, edi.nome 
    ORDER BY QuantidadeLivros DESC
    LIMIT 5
    ```

  - **Resultado**:

    [Tabela - Etapa 2](./Exercicios/Exportacao-de-dados/etapa2-editoras_com_mais_livros.csv)
    | CodEditora | NomeEditora | QuantidadeLivros |
    |:----------:|:-----------:|:----------------:|
    |     13     |     CBMM    |        138       |
    |      1     |     Ática   |         30       |
</details>
<br>

# 👁‍🗨 Evidências

<details>
<summary style="font-weight: bold;">📚 Caso de Estudo Biblioteca
</summary>

  <details>
  <summary>Exercício 1 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma"

  Deste modo, minha lógica para chegar à resolução foi de primeiro identificar as colunas que eu iria utilizar, usando  o diagrama DER eu fiz o FROM e o SELECT. Após isso, fiz a condição de filtragem usando o WHERE onde só pega datas depois de 31/12/2014, mostrando os resultados ordenados de forma crescente pelo código do livro.<br>
  E pode-se confirmar seguindo o link da imagem abaixo.
  </details>

  ![Evidencia 1](./Exercicios/Caso-biblioteca/imagens-execucao/exercicio1-sql.png)

  <details>
  <summary>Exercício 2 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor."

  A resolução foi bem simples, para listar os mais caros utilizei um ORDER BY do valor de forma Decrescente e usei LIMIT 10 para só mostrar os 10 mais caros.<br>
  E pode-se confirmar seguindo o link da imagem abaixo.
  </details>


  ![Evidencia 2](./Exercicios/Caso-biblioteca/imagens-execucao/exercicio2-sql.png)

  <details>
  <summary>Exercício 3 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente."

  Para a resolução, eu uni as tabelas Livro, Editora e Endereco usando o LEFT JOIN, limitei para 5 com LIMIT, contei todos os livros usando o COUNT( ) e ordenei de forma decrescente e por fim agrupei pelas colunas da tabela Editora e Endereco. Assim mostrando as 5 editoras com mais livros.<br>
  E pode-se confirmar seguindo o link da imagem abaixo.
  </details>

  ![Evidencia 3](./Exercicios/Caso-biblioteca/imagens-execucao/exercicio3-sql.png)

  <details>
  <summary>Exercício 4 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria). Utilize replace."

  Para a resolução, fiz a contagem de livro que cada autor tinha utilizando uma subquery no select, onde usei a função COUNT( ), nomeando essa subquery como "quantidade". Apresentei as colunas desejadas e por fim ordenei de forma crescente (por padrão o ASC é opcional), com o complemento do REPLACE( ) para retirar os acentos agudos na letra A das strings.<br>
  E pode-se confirmar seguindo o link da imagem abaixo.
  </details>

  ![Evidencia 4](./Exercicios/Caso-biblioteca/imagens-execucao/exercicio4-sql.png)

  <details>
  <summary>Exercício 5 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno."

  Na resolução, a primeira coisa foi colocar o DISTINCT para unicidade dos dados, em seguida uni as tabelas Autor, Livro, Editora e Endereco com o JOIN. Após isso, fiz uma condição de negação lógica para que fosse mostrados todos os autores com livros em editora que não são da região sul (utilizei NOT IN), por fim, ordenei em ordem crescente pelo nome dos autores.<br>
  E pode-se confirmar seguindo o link da imagem abaixo.
  </details>

  ![Evidencia 5](./Exercicios/Caso-biblioteca/imagens-execucao/exercicio5-sql.png)

  <details>
  <summary>Exercício 6 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes".

  Utilizei HAVING ao invés de WHERE para caso houvesse algum outro autor que pudesse empatar na maior quantidade de livros com outro autor. Eu fiz a conexão entre as tabelas usando o JOIN e agrupei por codigo do autor e nome, fazendo a contagem também de livros por cada autor. Utilizando o HAVING utilizei o comando `HAVING COUNT(liv.cod) = (...)` para que ele filtrasse apenas os autores que tivessem o resultado da subquery. Dentro dos parênteses que é o ponto chave, fiz uma subquery para selecionar o maior número `SELECT MAX(qtd)` da contagem de `SELECT count(*) AS qtd` da tabela livro agrupada por cada autor. Dessa forma, o Having( ) irá retornar algo como "depois de agrupar por autor,
  mantenha apenas os autores que têm exatamente o número máximo de publicações totais".<br>
  Não utilizei o WHERE, pois isso caberia utilizar o LIMIT, ao qual num empate decidiria por um dos dois e não os dois (que é o correto).<br>
  E pode-se confirmar seguindo o link da imagem abaixo.
  </details>

  ![Evidencia 6](./Exercicios/Caso-biblioteca/imagens-execucao/exercicio6-sql.png)

  <details>
  <summary>Exercício 7 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente"

  Para a resolução, uni as duas tabelas (Livro e Autor) usando o JOIN e condicionei com o WHERE para que somente aqueles autores que tivesse o código do livro como NULL fossem mostrados, ou seja, àqueles com nenhuma publicação. Utilizar o atributo `liv.publicacao` também funcionaria (neste caso), mas o recomendado é utilizar a Primary Key. Depois disso, ordenei crescentemente pelos nomes dos autores.
  </details>

  ![Evidencia 7](./Exercicios/Caso-biblioteca/imagens-execucao/exercicio7-sql.png)
</details>

<br>

<details>
<summary style="font-weight:bold">🛒 Caso de Estudo Loja</summary>

  <details>
  <summary>Exercício 8 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd."

  Assim como no exercício 6, utilizei o HAVING para resolver o problema, onde da mesma forma será mostrado todos os vendedores que tiverem no TOP 1, já que, se utilizasse o LIMIT, o LIMIT teria que decidir por qual deles do empate seria mostrado, o que não seria o correto.
  </details>

  ![Evidencia 8](./Exercicios/Caso-loja/imagens-execucao/exercicio8-sql.png)

  <details>
  <summary>Exercício 9 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro."

  Para a resolução deste, utilizei a mesma lógica do anterior, onde o uso do HAVING foi indispensável, uma vez que novamente pedia para que o produto mais vendido fosse mostrado. Visando a possibilidade de ter empates, o HAVING( ) foi necessário para fazer a filtragem sem o uso de LIMIT. Dentro do HAVING fiz subqueries, onde a primeira faz a soma da quantidade das vendas com a condição da DATA e o status de CONCLUIDO (chama-se total), e a segunda pega esse total e seleciona o valor máximo. Por fim, o HAVING( ) compara se a soma das quantidades de vendas é igual à esse valor máximo, se for, esse produto será mostrado.
  O REPLACE e LOWER foi para tratar os dados, caso houvessem status variáveis, como "Concluido" e "concluído".
  </details>

  ![Evidencia 9](./Exercicios/Caso-loja/imagens-execucao/exercicio9-sql.png)

  <details>
  <summary>Exercício 10 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. <br>
  Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.<br>
  As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal."

  Para a resolução deste, utilizei a função ROUND( ) para arredondar os números para até 2 casas decimais e o SUM( ) para somar o total da multiplicação de cada quantidade de produto vezes o seu valor unitário. Desta vez utilizei o LIKE para comparação da condição WHERE, na qual puxaria qualquer status que tivesse a entrada "conclu".
  </details>

  ![Evidencia 10](./Exercicios/Caso-loja/imagens-execucao/exercicio10-sql.png)

  <details>
  <summary>Exercício 11 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente."
  
  Neste exercício, ao invés de usar o HAVING e uma subquery no FROM, utilizei o WITH para criar uma "tabela fantasma" chamada gasto_por_cliente, onde fazia a seleção das colunas `cdcli` e `nmcli`, além de que 'gasto' era o resultado da somatória dos valores das vendas (quantidade X valor unitário do produto).<br>
  Depois disso, na query principal, fiz um FROM para essa tabela fantasma e filtrei utilizando o WHERE, que comparava se o gasto era igual ao valor máximo atingido, caso fosse, o Nome, Codigo e Gasto do cliente seria mostrado.
  </details>

  ![Evidencia 11](./Exercicios/Caso-loja/imagens-execucao/exercicio11-sql.png)

  <details>
  <summary>Exercício 12 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
  Observação: Apenas vendas com status concluído."
  
  Utilizei novamente o WITH para criar uma tabela temporária que nomeei de *vendas_por_vendedor*, onde fiz a somatória do total de vendas. Depois disso, na query principal utilizei um WHERE para condição e para comparar esse valor com o retorno da subquery, subquery essa que pegava o menor valor dessa somatória de vendas que não fosse zero. Trazendo assim, os dependentes do vendedor com menor valor bruto.
  </details>

  ![Evidencia 12](./Exercicios/Caso-loja/imagens-execucao/exercicio12-sql.png)

  <details>
  <summary>Exercício 13 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas."
  
  A lógica deste foi bem simples, então utilizei o básico para chegar ao resultado. Selecionei as colunas que seriam utilizadas, fiz a somatória das quantidades de vendas por produto e filtrei no WHERE utilizando o IN e o LIKE, por fim agrupei com o GROUP BY e usei o ORDER BY + LIMIT pra mostrar os 10 menos vendidos.
  </details>

  ![Evidencia 13](./Exercicios/Caso-loja/imagens-execucao/exercicio13-sql.png)

  <details>
  <summary>Exercício 14 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
  Observação: Apenas vendas com status concluído."
  
  Este também foi simples. Utilizei logo no SELECT as funções ROUND( ) AVG( ) acopladas para calcular o gasto médio. Depois disso, fiz a condição de filtragem usando o WHERE e ordenei em forma decrescente pelo gasto médio.
  </details>

  ![Evidencia 14](./Exercicios/Caso-loja/imagens-execucao/exercicio14-sql.png)

  <details>
  <summary>Exercício 15 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente."
  
  Neste exercício, utilizei o WHERE para filtrar apenas as vendas que foram deletadas (correspondente ao número 1, ao qual significa true em binário, já que a coluna era somente 0 ou 1) e ordenei crescentemente pelo codigo da venda (cdven).
  </details>

  ![Evidencia 15](./Exercicios/Caso-loja/imagens-execucao/exercicio15-sql.png)

  <details>
  <summary>Exercício 16 - Ao resolver o exercicio, foi solicitado para:</summary>

  > "Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).
  Obs: Somente vendas concluídas."
  
  Para a resolução deste exercício, utilizei a função de agregação AVG( ) para calcular a quantidade média vendida de cada produto. Esse valor foi arredondado para quatro casas decimais utilizando a função ROUND( ), conforme solicitado no enunciado.
  Em seguida, fiz a filtragem das vendas utilizando a cláusula WHERE, garantindo que apenas vendas com status concluído fossem consideradas no cálculo. Após isso, agrupei os dados pelas colunas estado e nome do produto, de modo que a média fosse calculada corretamente para cada combinação de estado e produto.
  Por fim, ordenei os resultados primeiramente pelo estado e, em seguida, pelo nome do produto, assegurando uma apresentação organizada e de fácil leitura dos dados retornados pela consulta.
  </details>

  ![Evidencia 16](./Exercicios/Caso-loja/imagens-execucao/exercicio16-sql.png)

</details>
<br>

<details><summary style="font-weight: bold;">🎲 Exportação de Dados</summary>

<details><summary>Etapa 1 - Explicação</summary>
  
  Para a resolução deste, no SELECT coloquei todas as colunas necessárias (com aliases) e fiz o JOIN das tabelas Livro, Editora e Autor. Depois disso, ordenei em ordem decrescente pelo valor dos livros e limitei para mostrar apenas 10.
</details>


![Etapa 1 - Execução e Resolução](./Exercicios/Exportacao-de-dados/imagens-execucao/resolucao-etapa1.png)


<details><summary>Etapa 2 - Explicação</summary>
  
  Para a resolução deste, no SELECT fiz a contagem da quantidade de livros utilizando a função COUNT() e coloquei as colunas que precisavam aparecer (com aliases). Depois disso fiz a conexão entre as tabelas Editora e Livro com o JOIN e agrupei por código das Editoras e pelos seus nomes, ordenando decrescentemente pela quantidade de livros de cada uma. E utilizei o LIMIT para mostrar apenas 5.
</details>


![Etapa 2 - Execução e Resolução](./Exercicios/Exportacao-de-dados/imagens-execucao/resolucao-etapa2.png)


</details>

<br>

# 🎯 Desafio da Sprint
O desenvolvimento do desafio da sprint e seus respectivos arquivos relacionados encontram-se em sua pasta, assim como seu README que fora usado para dissertar sobre os passos executados e resultados.
O Desafio foi desenvolvido em duas etapas fundamentais: Modelo Relacional e Modelo Dimensional.
- 📁[Pasta do Desafio](../Sprint%202/Desafio/)
- 📝[README do Desafio](../Sprint%202/Desafio/README.md)

<br>

# ✅ Certificados
Não houve cursos externos, apenas dentro da Compass Udemy.