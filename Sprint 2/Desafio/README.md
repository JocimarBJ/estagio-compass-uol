# [Exercícios](./Desafio.txt)

### Exercício 1
No primeiro exercício foi proposto que selecionássemos os nomes das cidades de forma única, onde existem na tabela de *sales.customers* com a condição de que fossem do estado de Minas Gerais, ordenando a consulta em ordem alfabética. 

1. **Passo a Passo até o resultado**
    
    Primeiramente tive que buscar no **pgAdmin** as colunas e tabelas que precisaria saber para fazer a consulta. Então identifiquei as colunas *city* e *state*, além da tabela *customers* contida no schema *sales*.
    <br>
    Identificado as colunas, precisei identificar quais comandos utilizaria. Logo, identifiquei `SELECT DISTINCT`, `FROM`, `WHERE` e `ORDER BY`.
    <br>
    Então, baseando-se no conhecimento que já tinha e nas aulas recém vistas realizei o script que faria a consulta.

2. **Explicação do código**

    Nessa parte pode-se perceber com esse código que utilizei o `SELECT DISTINCT` para evitar informações redundantes, o `FROM` para informar de onde deveria ser buscado, o `WHERE` para condicionar e filtrar as cidades mostrando apenas as que tivessem o *state* igual à *' MG '* e o `ORDER BY` para ordernar de forma crescente (default) as cidades de A-Z:
    ```SQL
    SELECT DISTINCT city 
    FROM sales.customers 
    WHERE state = 'MG' 
    ORDER BY city
    ```

    Obtendo assim o seguinte retorno:
    <details>
    <summary>Clique aqui para ver</summary>
    
    ![evidencia do resultado - exercicio 1](../Evidencias/evidencia%201.png)

    </details>

### Exercício 2

No segundo exercício foi proposto que fizéssemos a consulta utilizando o *visit_id*, filtrando as 10 compras mais recentes efetuadas.

1. **Passo a Passo até o resultado**

    Seguindo a mesma lógica do primeiro exercício, identifiquei os comandos e tabelas necessárias para a consulta.

2. **Explicação do código**

    Com este código, note que utilizei um `SELECT` normal, já que não havia sido solicitado a unicidade dos dados seguido da coluna *visit_id*, o `FROM` da coluna correspondente às compras/funil de vendas (*sales.funnel*), em seguida o `WHERE` de *paid_date* 

    ```SQL
    SELECT visit_id
    FROM sales.funnel 
    WHERE paid_date IS NOT NULL 
    ORDER BY paid_date DESC 
    LIMIT 10
    ```