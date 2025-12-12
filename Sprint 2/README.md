# 📝 Resumo

## 📊 SQL Para Análise de Dados
### 🔧Configuração do ambiente de trabalho
Como meu pgAdmin já estava instalado na minha máquina, eu somente fiz a revisão do que foi passado para ver se não havia ausência de algum fator fundamental para a execução dos futuros exercícios;
### ⌨️ Comandos básicos
A maioria dos comandos, como Select, Where, Order By eu já conhecia, no entanto pude aprender como funcionava o Limit e o Distinct.
- Podemos utilizar o asterísco `*` quando desejamos printar todas as colunas da tabela e seus dados.
- **SELECT** usamos frequentemente na linguagem SQL, serve para selecionarmos colunas de tabelas e mostrar os dados filtrados. 
  - Exemplo: `SELECT usernames FROM game.users`.
- o **WHERE** é utilizado em conjunto com o Select e serve para filtrar as linhas da tabela de acordo com a condição que você impõe. 
  - Exemplo: `SELECT email, state FROM sales.customers WHERE state = 'SC'`. 

  Dessa forma, somente àqueles que corresponderem com a sigla SC será mostrado.
- **DISTINCT** serve para remover linhas duplicadas, mostrando apenas as linhas que distinguem, evitando que informações se repitam. Utilizado logo após o SELECT. 
  - Exemplo: `SELECT DISTINCT brand FROM sales.products`.
- **ORDER BY** serve para ordenar de acordo com a regra definida, por exemplo decrescente, crescente e etc.
- **LIMIT** é utilizado para limitar o número de linhas da consulta. Utilizado sempre no final da linha.

Houveram demais informações e detalhes durante as aulas, como: não utilizar virgula antes do FROM e etc. Algo que observei não ser retratado foi que uma boa prática para comandos SQL é utilizar eles em maiúsculo, por exemplo: `SELECT email FROM ...` ao invés de `Select Email FROM ...`, visando a organização e formatação textual, como uma melhor compreensão e praticidade para qualquer desenvolvedor que estiver lendo.

### ➗ Operadores
Temos diversos tipos de operadores, sendo eles **aritméticos, comparação e lógicos**.
Eles servem para executarmos cálculos matemáticos, comparar valores retornando *true* ou *false* e unir expressões simples em uma composta. <br>
São muitos, mas podemos citar alguns como, respectivamente:

- ``` ||, +, -, *, /, ^, %...```
- ``` =, <=, =>, <>, >, <...```
- ``` AND, OR, NOT, IN, ON, LIKE, USING... ```

### 🔁Funções Agregadas
Existem vários tipos de funções agregadas, sendo elas: Count(), Sum(), Min(), Max(), Avg(), Group By e Having.
- `COUNT( )` serve para contabilizar
- `SUM( )` serve para somar
- `MIN( )` pega o menor/calcula o mínimo
- `MAX( )` pega o máximo/calcula o máximo
- `AVG( )` calcula a média
- `GROUP BY`: serve para agrupar os registros semelhantes da coluna. Se usado somente ele, funciona como o DISTINCT
- `HAVING`: serve para filtrar as linhas de seleção por uma coluna já agregadas. Diferente do WHERE que só pode filtrar colunas não agregadas, a função HAVING pode filtrar tanto colunas agregadas como não agregadas.

As funções agregadas não computam células NULL como zero, elas ignoram.

### ⚙️ Join
Existem 4 tipos de Join para serem utilizados no SQL, sendo eles:
- ⟗ `FULL JOIN` pega todos os dados, tanto da tabela da esquerda (tabela declarada primeiro) e tabela da direita (tabela declarada depois)
- ⟕ `LEFT JOIN` pega todos os dados da tabela da esquerda, e da tabela da direita pega somente aqueles correspondentes à tabela da esquerda.
- ⨝ `INNER JOIN` pega a intersecção de dados entre a tabela Left e a tabela Right
- ⟖ `RIGHT JOIN` pega todos os dados da tabela da direita, mesma coisa do Left Join, porém o contrário.

São mais comumente utilizados o Left Join e o Inner Join. Além disso, baseando-se nesses 4 comandos de Join, podemos conseguir uma variação de até 8 jeitos diferentes de extrair os dados na consulta, como:
`USING, NATURAL JOIN, SELF JOIN, CROSS JOIN, OUTER JOIN`

### <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Venn_0111_1111.svg/250px-Venn_0111_1111.svg.png" width="18" style="vertical-align: middle"/> Unions
O comando ``UNION`` serve basicamente para unir uma tabela sobre a outra, desde que tenham a mesma quantidade de colunas e essas colunas sejam do mesmo tipo.
Existe o `UNION ALL` e o `UNION`, sendo sua principal diferença que o UNION ALL não checa e remove as linhas duplicadas.

*É recomendado utilizar somente o UNION ALL quando sabemos que o conteúdo das tabelas são diferentes.*

### 🔀 Subqueries
As Subqueries servem para que possamos consultar os dados de outras consultas que estão embutidas, ou seja, utilizar os resultados de uma query dentro de outra query.
Existem 4 tipos de Subquery, basicamente são no: Where, With, From e Select.

Alguns pontos de atenção seriam:
- Sempre ao utilizar no WHERE, a Subquery deve retornar apenas um valor, não mais que uma linha ou coluna.
- Subqueries com WITH é muito mais legível e cria como se fosse uma "tabela fantasma"
- Não é recomendado utilizar Subquery no FROM, já que toda subquery no FROM pode ser substituída por uma com WITH
- A Subquery no SELECT é bem pesada, é como se estivesse rodando uma query a cada linha. Algumas vezes é o único jeito de responder uma pergunta, mas é bom evitar usar. Além disso, ela só pode retornar um dado, como no caso do WHERE.

### 🔄 Tratamento de Dados

- **Conversão de Unidades**: <br>
  Existem dois jeitos de conversão (type casting), uma das formas utiliza `::` e na outra a função `CAST()`, basicamente. Existem outras funções, que serão citadas mais a abaixo.
  - Para utilizar o `::`, devemos seguir o seguinte padrão `dado_da_tabela::formato_pretendido`. Exemplo: `112233::text`.
  - Para utilizar o Cast(), devemos:
    ```SQL
    CAST(dado_seu AS formato_pretendido)

    Exemplo: SELECT CAST(20050124 AS DATE)
    ```

- **Tratamento Geral**:<br>
  Nesta parte utilizamos dois tipos, sendo eles CASE WHEN e COALESCE( )
  - `CASE WHEN` é usado para agrupamento de dados. No primeiro When a condição deve ser verdadeira e qual resultado esperamos caso ela seja verdadeira. A lógica é bem parecida com SWITCH CASE nas linguagens de programação. No CASE WHEN nós utilizamos os operadores lógicos e deve sempre ser finalizado com END.
  - `COALESCE( )` é usado para tratamento de dados nulos. Dentro do COALESCE pode-se colocar uma sequência de valores separados por vírgula. Primeiro, ele verifica qual é o primeiro campo não nulo de uma lista de valores e vai retornando valor por valor que não seja nulo, todos que ele considerar nulo ele vai ignorar e trocando os valores nulos pelo primeiro não nulo dentro do parênteses. Exemplo:
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

- **Tratamento de Texto**:<br>
LOWER( ), UPPER( ), TRIM( ), REPLACE( ) são algumas das formas de tratamento de texto apresentadas.
  - `LOWER()` basicamente deixa toda a string em minúsculo
  - `UPPER()` deixa toda a string em maiúsculo
  - `TRIM()` retira os espaços em brancos das extremidades de uma string
  - `REPLACE()` substitui a parte da string passada no parâmetro, juntamente com o que queremos colocar no lugar.<br>
  Exemplo: 
      ```SQL
      REPLACE('SAO PAULO', 'SAO', 'SÃO') = 'SÃO PAULO'
      -- irá retornar TRUE
      ```

- **Tratamento de Datas**:<br>
Existem 4 funções muito utilizadas para tratar datas e horas, sendo elas:
  - `interval()` serve para definir um intervalo específico de tempo, por exemplo, quando você quer somar semanas, meses, horas, anos e etc, ao invés de apenas dias (default).
  - `date_trunc()` trunca as datas, por exemplo, caso queira que "corte" por mês, por ano e etc.
  - `extract()` serve para extrair as unidades de uma data, ou seja, se você quer saber qual dia da semana aquela data se refere, você pode utilizar o extract( ), onde ele retornará um número representativo.
  - `datediff()` calcula a diferença entre datas, mas diferente de apenas utilizar o operador de subtração, utilizar o datediff( ) nos dá a possibilidade e maior clareza de especificar qual diferença queremos que retorne informando o período, por exemplo, a diferença de semanas, meses, anos e etc, só de utilizar strings como *weeks*, *months* e *years*.

- **Funções**:<br>
As funções servem para criarmos comandos personalizados de scripts que serão usados comumente. No entanto, devido à sua complexidade de criação não é algo que usamos com muita frequência, mas quando precisamos é sempre mais prático.

  Para criarmos uma função, precisamos de algumas coisas antes:
  - Definir que tipo de função será e para qual finalidade
  - Criar o escopo da consulta para ter certeza do caminho que irá seguir
  - Definir um nome para ela que torne claro a sua funcionalidade e não traga ambiguidade
  - Definir quais serão as variáveis de entrada passadas por parâmetro e as variáveis de saída

  - Exemplo Prático:
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

### Manipulação de Tabelas:
- **Tabelas - Criação e Deleção:**<br>
  Existem 2 formas de criar uma tabela:
  - A partir de uma Query: Após fazer a query, utilizamos o comando `INTO` + nome_que_queremos antes do FROM. Após isso, ao invés de sempre termos que fazer uma query para obter o mesmo resultado, podemos simplesmente invocar a tabela com o nome que colocamos.
  - A partir do Zero: Usamos o comando `CREATE TABLE nome_que_queremos(variavel1 tipo 1, variavel2 tipo2,...)`. No entanto, a tabela estará vazia, então para preenchê-la usamos:
    ```SQL
    INSERT INTO nome_que_colocamos(parâmetro1, parâmetro2,...)
    VALUES(valor1, valor1_modificado)(valor2, valor2_modificado...)
    ```
  - Para excluir a tabela usamos `DROP TABLE nome_que_usamos`

- **Linhas - Inserção, Atualização e Deleção:**<br>
  - Para inserir linhas, a sintaxe é parecida, utilizamos:
    ```SQL
    INSERT INTO nome_da_tabela(parametro1, parametro2) VALUES (valor1, valor1_modificado...)
    ```
  - Para atualizar alguma informação de uma linha, usamos:
    ```SQL
    UPDATE nome_da_tabela
    SET coluna = dado_modificado 
    WHERE coluna2 = dado_correspondente
    ```
  - Para deletar, usamos:
    ```SQL
    DELETE FROM nome_da_tabela
    WHERE coluna1 = dado_correspondente
    ```
    
- **Colunas - Inserção, Atualização e Deleção:**<br>
  - Para inserirmos colunas em uma tabela, usamos:
    ```SQL
    ALTER TABLE nome_da_tabela
    ADD nome_da_coluna tipo_da_coluna
    ```
  - Para atualizarmos/inserirmos dados de uma coluna:
    ```SQL
    UPDATE nome_da_tabela
    SET nome_da_coluna = dado_que_voce_quer
    WHERE true 
    --true serve para quando queremos que todas as linhas sejam atualizadas.
    ```
    Se quisermos por exemplo atualizar o tipo da coluna ou renomeá-la:
    ```SQL
    --Alterar tipo
    ALTER TABLE nome_da_tabela
    ALTER COLUMN nome_da_coluna type tipo

    --Renomear
    ALTER TABLE nome_da_tabela
    RENAME COLUMN nome_da_coluna TO novo_nome
    ```
  - Para deletar uma coluna, usamos: `ALTER TABLE nome_da_tabela DROP COLUMN nome_da_coluna`
# PB - AWS 2/10
### Conceitos da Linguagem Python

### Conceitos do Dia-a-Dia de um Data & Analytics

# Exercícios
### Python

1. Durante o
[Exercício 1 - Parte 1](./Exercicios/Exercício%2001-SELECT.txt)

2. ...
[Resposta Ex2.](./Exercicios/Exercício%2002-DISTINCT.txt)

### SQL

# Evidências

Ao executar o código do exercício ... observei que ... conforme podemos ver na imagem a seguir:

![Evidencia 1](./Evidencias/sample.webp)

## Demais pastas:
**Certificados**: Não houve cursos externos, apenas dentro da Compass Udemy.