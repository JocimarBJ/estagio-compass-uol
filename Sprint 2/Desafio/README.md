# ⏬ Etapas do Desafio da Sprint 2


###  [Etapa 1 - Normalização e DER](./Etapa%201%20-%20Relacional/)
    
- [Arquivo do Diagrama](./Etapa%201%20-%20Relacional/concessionaria_DER.erd)
    (Utilize a extensão 
    [ERD Editor](https://marketplace.visualstudio.com/items?itemName=dineug.vuerd-vscode) 
    no VSCode para visualizá-lo)
#### 🎨 [Diagramação](../Evidencias/Etapa%201%20-%20Relacional/diagrama_modelo_relacional_normalizado.png)
- Durante esta etapa eu desenvolvi o Diagrama Entidade-Relacionamento, primeiramente, identificando possíveis entidades através dos atributos da tabela base original. Dessa forma, destrinchei-a em outras tabelas, tais quais: `tb_Carro`, `tb_Vendedor`, `tb_Locacao`, `tb_Combustivel`, `tb_Cliente`.
    <br>
    Pode-se observar tal fato através da imagem abaixo.
    <details><summary style="font-weight: bold;"> 📌Diagrama Entidade-Relacionamento Normalizado</summary>
    
    ![Evidência DER](../Evidencias/Etapa%201%20-%20Relacional/diagrama_modelo_relacional_normalizado.png)
    </details>

#### 👨‍💻 [Modelo Físico (SQLite)](../Desafio/Etapa%201%20-%20Relacional/modelo_relacional_normalizado.sql)
-  Após feito o DER, implementei as tabelas com SQL de acordo, transicionando assim do Modelo Lógico para o Modelo Físico. A diferença entre os dois, além do uso das funções e comandos, foi a especifição dos parâmetros de cada atributo, bem como suas limitações ou exigências. Além disso, todos os dados anteriores foram movidos para essa nova base de dados normalizada, utilizando INSERT INTO nas tabelas.<br>
Segue abaixo o passo a passo realizado por mim durante esta parte do desafio.

    <details><summary style="font-weight: bold;">Código</summary>

    ```SQL
    -- concessionaria_normalizada.db
    -- sqlite

    ------ CONSULTAS ---------
    SELECT * FROM tb_Combustivel AS tbcom

    SELECT * FROM tb_Cliente AS tbcli

    SELECT * FROM tb_Vendedor AS tbven

    SELECT * FROM tb_Carro AS tbcar

    SELECT * FROM tb_Locacao AS tbloc

    ------ CRIANDO E NORMALIZANDO --------
    -- TABELA COMBUSTÍVEL
    CREATE TABLE tb_Combustivel (
    idCombustivel   INT,
    tipoCombustivel VARCHAR(20) NOT NULL,
    PRIMARY KEY (idCombustivel)
    );

    -- TABELA CLIENTE
    CREATE TABLE tb_Cliente (
    idCliente     INT,
    nomeCliente   VARCHAR(100)  NOT NULL,
    cidadeCliente VARCHAR(50)   NOT NULL,
    estadoCliente VARCHAR(50)   NOT NULL,
    paisCliente   VARCHAR(50)   NOT NULL,
    PRIMARY KEY (idCliente)
    );

    -- TABELA VENDEDOR
    CREATE TABLE tb_Vendedor (
    idVendedor      INT,
    nomeVendedor    VARCHAR(100) NOT NULL,
    sexoVendedor    SMALLINT     NOT NULL,
    estadoVendedor  VARCHAR(50)  NOT NULL,
    PRIMARY KEY (idVendedor)
    );

    -- TABELA CARRO
    CREATE TABLE tb_Carro (
    idCarro       INT,
    chassiCarro   VARCHAR(30) NOT NULL,
    marcaCarro    VARCHAR(50) NOT NULL,
    modeloCarro   VARCHAR(50) NOT NULL,
    anoCarro      INT         NOT NULL,
    idCombustivel INT         NOT NULL,
    PRIMARY KEY (idCarro),
    FOREIGN KEY (idCombustivel) REFERENCES tb_Combustivel(idCombustivel)
    );

    -- TABELA LOCAÇÃO
    CREATE TABLE tb_Locacao (
    idLocacao   INT,
    dataLocacao DATE          NOT NULL,
    horaLocacao TIME          NOT NULL,
    qtdDiaria   INT           NOT NULL,
    vlrDiaria   DECIMAL(10,2) NOT NULL,
    dataEntrega DATE          NOT NULL,
    horaEntrega TIME          NOT NULL,
    kmCarro     INT           NOT NULL,
    idCliente   INT           NOT NULL,
    idVendedor  INT           NOT NULL,
    idCarro     INT           NOT NULL,
    PRIMARY KEY (idLocacao),
    FOREIGN KEY (idCliente)   REFERENCES tb_Cliente(idCliente),
    FOREIGN KEY (idVendedor)  REFERENCES tb_Vendedor(idVendedor),
    FOREIGN KEY (idCarro)     REFERENCES tb_Carro(idCarro)
    );

    -- Combustível Dados
    INSERT INTO tb_Combustivel (idCombustivel, tipoCombustivel) VALUES
    (1,'Gasolina'),
    (2,'Etanol'),
    (3,'Flex'),
    (4,'Diesel');

    -- Cliente Dados
    INSERT INTO tb_Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES
    (2,'Cliente dois','São Paulo','São Paulo','Brasil'),
    (3,'Cliente tres','Rio de Janeiro','Rio de Janeiro','Brasil'),
    (4,'Cliente quatro','Rio de Janeiro','Rio de Janeiro','Brasil'),
    (5,'Cliente cinco','Manaus','Amazonas','Brasil'),
    (6,'Cliente seis','Belo Horizonte','Minas Gerais','Brasil'),
    (10,'Cliente dez','Rio Branco','Acre','Brasil'),
    (20,'Cliente vinte','Macapá','Amapá','Brasil'),
    (22,'Cliente vinte e dois','Porto Alegre','Rio Grande do Sul','Brasil'),
    (23,'Cliente vinte e tres','Eusébio','Ceará','Brasil'),
    (26,'Cliente vinte e seis','Campo Grande','Mato Grosso do Sul','Brasil');

    -- Vendedor Dados
    INSERT INTO tb_Vendedor (
    idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES
    (5,'Vendedor cinco',0,'São Paulo'),
    (6,'Vendedora seis',1,'São Paulo'),
    (7,'Vendedora sete',1,'Rio de Janeiro'),
    (8,'Vendedora oito',1,'Minas Gerais'),
    (16,'Vendedor dezesseis',0,'Amazonas'),
    (30,'Vendedor trinta',0,'Rio Grande do Sul'),
    (31,'Vendedor trinta e um',0,'Ceará'),
    (32,'Vendedora trinta e dois',1,'Mato Grosso do Sul');

    -- Carro Dados
    INSERT INTO tb_Carro
    (idCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES
    (98,'AKJHKN98JY76539','Fiat','Fiat Uno',2000,1),
    (99,'IKJHKN98JY76539','Fiat','Fiat Palio',2010,1),
    (3,'DKSHKNS8JS76S39','VW','Fusca 78',1978,1),
    (10,'LKIUNS8JS76S39','Fiat','Fiat 147',1996,1),
    (7,'SSIUNS8JS76S39','Fiat','Fiat 147',1996,1),
    (6,'SKIUNS8JS76S39','Nissan','Versa',2019,1),
    (2,'AKIUNS1JS76S39','Nissan','Versa',2019,2),
    (4,'LLLUNS1JS76S39','Nissan','Versa',2020,2),
    (1,'AAAKNS8JS76S39','Toyota','Corolla XEI',2023,3),
    (5,'MSLUNS1JS76S39','Nissan','Frontier',2022,4);

    -- Locação Dados
    INSERT INTO tb_Locacao
    (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro, idCliente, idVendedor, idCarro)
    VALUES
    (1,'2015-01-10','10:00',2,100,'2015-01-12','10:00',25412,2,5,98),
    (2,'2015-02-10','12:00',2,100,'2015-02-12','12:00',29450,2,5,98),
    (3,'2015-02-13','12:00',2,150,'2015-02-15','12:00',20000,3,6,99),
    (4,'2015-02-15','13:00',5,150,'2015-02-20','13:00',21000,4,6,99),
    (5,'2015-03-02','14:00',5,150,'2015-03-07','14:00',21700,4,7,99),
    (6,'2016-03-02','14:00',10,250,'2016-03-12','14:00',121700,6,8,3),
    (7,'2016-08-02','14:00',10,250,'2016-08-12','14:00',131800,6,8,3),
    (8,'2017-01-02','18:00',10,250,'2017-01-12','18:00',151800,4,6,3),
    (9,'2018-01-02','18:00',10,280,'2018-01-12','18:00',152800,4,6,3),
    (10,'2018-03-02','18:00',10,50,'2018-03-12','18:00',211800,10,16,10),
    (11,'2018-04-01','11:00',10,50,'2018-04-11','11:00',212800,20,16,7),
    (12,'2020-04-01','11:00',10,150,'2020-04-11','11:00',21800,20,16,6),
    (13,'2022-05-01','08:00',20,150,'2022-05-21','18:00',10000,22,30,2),
    (14,'2022-06-01','08:00',20,150,'2022-06-21','18:00',20000,22,30,2),
    (15,'2022-07-01','08:00',20,150,'2022-07-21','18:00',30000,22,30,2),
    (16,'2022-08-01','08:00',20,150,'2022-08-21','18:00',40000,22,30,2),
    (17,'2022-09-01','08:00',20,150,'2022-09-21','18:00',55000,23,31,4),
    (18,'2022-10-01','08:00',20,150,'2022-10-21','18:00',56000,23,31,4),
    (19,'2022-11-01','08:00',20,150,'2022-11-21','18:00',58000,23,31,4),
    (20,'2023-01-02','18:00',10,880,'2023-01-12','18:00',1800,5,16,1),
    (21,'2023-01-15','18:00',10,880,'2023-01-25','18:00',8500,5,16,1),
    (22,'2023-01-25','08:00',5,600,'2023-01-30','18:00',28000,26,32,5),
    (23,'2023-01-31','08:00',5,600,'2023-02-05','18:00',38000,26,32,5),
    (24,'2023-02-06','08:00',5,600,'2023-02-11','18:00',48000,26,32,5),
    (25,'2023-02-12','08:00',5,600,'2023-02-17','18:00',68000,26,32,5),
    (26,'2023-02-18','08:00',1,600,'2023-02-19','18:00',78000,26,32,5);

    ```

    </details>


    <details><summary style="font-weight: bold;"> Criando Tabelas</summary>

    Observa-se que utilizei `NOT NULL` para garantir que todos os dados fosesm obrigatórios, fiz desta forma pois notei que não havia nenhum dado NULL na base de dados original, então considerei que todos eram considerados Não Vazios. Além disso, neste caso não foi necessário, mas é comum utilizar-se `AUTO_INCREMENT` nas chaves primárias, mas como o SQLite automaticamente já incrementa todos os atributos considerados Chaves Primárias, logo não foi preciso.
    
    Como foi utilizado o SQLite, se faz necessário para as máquinas que executarem tais códigos SQL o uso do comando para a ativação das `FOREIGN KEY`, tal qual é: 
    ```SQL
    PRAGMA foreign_keys = ON;
    ```
    Apesar de ser possível a execução sem a ativação, o problema está nas operações `INSERT`, `UPDATE` ou `DELETE` que posteriormente podem ocorrer, onde o SQLite simplesmente ignora a restrição durante essas operações. Por exemplo, caso esteja desativado, o SQLite aceita os comandos, mas permite que insira dados que violam a integridade (ex: cadastrar um pedido pra um cliente que não existe ainda).

    ![Criando Tabelas](../Evidencias/Etapa%201%20-%20Relacional/imagens-execucao/criando_tabelas.png)

    <details><summary>Código</summary>

    ```SQL
    ------ CRIANDO E NORMALIZANDO --------
    -- TABELA COMBUSTÍVEL
    CREATE TABLE tb_Combustivel (
    idCombustivel   INT,
    tipoCombustivel VARCHAR(20) NOT NULL,
    PRIMARY KEY (idCombustivel)
    );

    -- TABELA CLIENTE
    CREATE TABLE tb_Cliente (
    idCliente     INT,
    nomeCliente   VARCHAR(100)  NOT NULL,
    cidadeCliente VARCHAR(50)   NOT NULL,
    estadoCliente VARCHAR(50)   NOT NULL,
    paisCliente   VARCHAR(50)   NOT NULL,
    PRIMARY KEY (idCliente)
    );

    -- TABELA VENDEDOR
    CREATE TABLE tb_Vendedor (
    idVendedor      INT,
    nomeVendedor    VARCHAR(100) NOT NULL,
    sexoVendedor    SMALLINT     NOT NULL,
    estadoVendedor  VARCHAR(50)  NOT NULL,
    PRIMARY KEY (idVendedor)
    );

    -- TABELA CARRO
    CREATE TABLE tb_Carro (
    idCarro       INT,
    chassiCarro   VARCHAR(30) NOT NULL,
    marcaCarro    VARCHAR(50) NOT NULL,
    modeloCarro   VARCHAR(50) NOT NULL,
    anoCarro      INT         NOT NULL,
    idCombustivel INT         NOT NULL,
    PRIMARY KEY (idCarro),
    FOREIGN KEY (idCombustivel) REFERENCES tb_Combustivel(idCombustivel)
    );

    -- TABELA LOCAÇÃO
    CREATE TABLE tb_Locacao (
    idLocacao   INT,
    dataLocacao DATE          NOT NULL,
    horaLocacao TIME          NOT NULL,
    qtdDiaria   INT           NOT NULL,
    vlrDiaria   DECIMAL(10,2) NOT NULL,
    dataEntrega DATE          NOT NULL,
    horaEntrega TIME          NOT NULL,
    kmCarro     INT           NOT NULL,
    idCliente   INT           NOT NULL,
    idVendedor  INT           NOT NULL,
    idCarro     INT           NOT NULL,
    PRIMARY KEY (idLocacao),
    FOREIGN KEY (idCliente)   REFERENCES tb_Cliente(idCliente),
    FOREIGN KEY (idVendedor)  REFERENCES tb_Vendedor(idVendedor),
    FOREIGN KEY (idCarro)     REFERENCES tb_Carro(idCarro)
    );
    ```
    </details>
    
    </details>

    <details><summary style="font-weight: bold;">Inserindo Dados</summary>

    - Inserindo dados na Tabela Carro:

        ![Inserindo dados na Tabela Carro](../Evidencias/Etapa%201%20-%20Relacional/imagens-execucao/inserindo/inserindo_dados_tb_carro.png)

        <details><summary>Código</summary>

        ```SQL
        -- Carro Dados
        INSERT INTO tb_Carro
        (idCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES
        (98,'AKJHKN98JY76539','Fiat','Fiat Uno',2000,1),
        (99,'IKJHKN98JY76539','Fiat','Fiat Palio',2010,1),
        (3,'DKSHKNS8JS76S39','VW','Fusca 78',1978,1),
        (10,'LKIUNS8JS76S39','Fiat','Fiat 147',1996,1),
        (7,'SSIUNS8JS76S39','Fiat','Fiat 147',1996,1),
        (6,'SKIUNS8JS76S39','Nissan','Versa',2019,1),
        (2,'AKIUNS1JS76S39','Nissan','Versa',2019,2),
        (4,'LLLUNS1JS76S39','Nissan','Versa',2020,2),
        (1,'AAAKNS8JS76S39','Toyota','Corolla XEI',2023,3),
        (5,'MSLUNS1JS76S39','Nissan','Frontier',2022,4);
        ```
        </details>
        <br>

    - Inserindo dados na Tabela Cliente:
    
        ![Inserindo dados na Tabela Cliente](../Evidencias/Etapa%201%20-%20Relacional/imagens-execucao/inserindo/inserindo_dados_tb_cliente.png)
        <details><summary>Código</summary>

        ```SQL
        -- Cliente Dados
        INSERT INTO tb_Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES
        (2,'Cliente dois','São Paulo','São Paulo','Brasil'),
        (3,'Cliente tres','Rio de Janeiro','Rio de Janeiro','Brasil'),
        (4,'Cliente quatro','Rio de Janeiro','Rio de Janeiro','Brasil'),
        (5,'Cliente cinco','Manaus','Amazonas','Brasil'),
        (6,'Cliente seis','Belo Horizonte','Minas Gerais','Brasil'),
        (10,'Cliente dez','Rio Branco','Acre','Brasil'),
        (20,'Cliente vinte','Macapá','Amapá','Brasil'),
        (22,'Cliente vinte e dois','Porto Alegre','Rio Grande do Sul','Brasil'),
        (23,'Cliente vinte e tres','Eusébio','Ceará','Brasil'),
        (26,'Cliente vinte e seis','Campo Grande','Mato Grosso do Sul','Brasil');
        ```
        </details>
        <br>

    - Inserindo Dados na Tabela Combustivel:

        ![Inserindo dados na Tabela Combustivel](../Evidencias/Etapa%201%20-%20Relacional/imagens-execucao/inserindo/inserindo_dados_tb_combustivel.png)
        <details><summary>Código</summary>

        ```SQL
        -- Combustível Dados
        INSERT INTO tb_Combustivel (idCombustivel, tipoCombustivel) VALUES
        (1,'Gasolina'),
        (2,'Etanol'),
        (3,'Flex'),
        (4,'Diesel');
        ```
        </details>
        <br>

    - Inserindo dados na Tabela Vendedor:

        ![Inserindo dados na Tabela Vendedor](../Evidencias/Etapa%201%20-%20Relacional/imagens-execucao/inserindo/inserindo_dados_tb_vendedor.png)
        <details><summary>Código</summary>

        ```SQL
        -- Vendedor Dados
        INSERT INTO tb_Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES
        (5,'Vendedor cinco',0,'São Paulo'),
        (6,'Vendedora seis',1,'São Paulo'),
        (7,'Vendedora sete',1,'Rio de Janeiro'),
        (8,'Vendedora oito',1,'Minas Gerais'),
        (16,'Vendedor dezesseis',0,'Amazonas'),
        (30,'Vendedor trinta',0,'Rio Grande do Sul'),
        (31,'Vendedor trinta e um',0,'Ceará'),
        (32,'Vendedora trinta e dois',1,'Mato Grosso do Sul');
        ```
        </details>

    </details>
<br>

- Após as etapas da Diagramação, Criação e Inserção, foi o momento de executar e conferir se tudo estava encaixado conforme o previsto.<br>
Segue abaixo o sucesso da execução:
    <details><summary style="font-weight: bold;"> Obtive esse retorno </summary>

    ![amostra](../Evidencias/Etapa%201%20-%20Relacional/imagens-execucao/evidencia1_etapa1_execucao.png)

    </details>

<hr/>

### [Etapa 2 - Dimensional (Star Schema)](./Etapa%202%20-%20Dimensional/) 

- [Arquivo do Diagrama](./Etapa%202%20-%20Dimensional/concessionaria_DIM.erd) (Utilize a extensão 
    [ERD Editor](https://marketplace.visualstudio.com/items?itemName=dineug.vuerd-vscode) 
    no VSCode para visualizá-lo)

#### 🎨 [Diagramação](../Evidencias/Etapa%202%20-%20Dimensional/diagrama_modelo_dimensional.png)
- Após ter desenvolvido e normalizado a base de dados, iniciei a Modelagem Dimensional escolhendo qual modelo poderia ser o mais ideal para este caso, logo decidi que seria o **Star Schema**, uma vez que ele é mais recomendado visando desempenho e eficiência, algo que o Snowflake tem desvantagem. Comecei renomeando os atributos e nomes das tabelas para trazer mais clareza semântica, depois identifiquei qual seria a tabela evento/tabela fato, agrupei os atributos que fossem pertencentes às entidades ou ao evento e criei uma tabela `dim_tempo` como boa prática para modelagem dimensional, na qual teria apenas datas, horas e intervalos de tempos definidos.

    <details><summary style="font-weight: bold;"> 📌Diagrama Dimensional</summary>
    
    ![Evidência Diagrama Dimensional](../Evidencias/Etapa%202%20-%20Dimensional/diagrama_modelo_dimensional.png)
    </details>

#### 👨‍💻 [Modelo Físico (SQLite)](../Desafio/Etapa%202%20-%20Dimensional/modelo_dimensional.sql)
- Feito o diagrama dimensional, iniciei o processo do Modelo Físico, ao qual por recomendação utilizei `CREATE VIEW` para formar as tabelas e apresentá-las.
Observa-se que para o funcionamento da tabela `dim_tempo` utilizei uma CTE com `WITH` que é recursiva para ela registrar de um intervalo de data à outro, hora por hora. Criei as tabelas `dim_cliente`, `dim_vendedor`, `dim_carro` e a tabela `fato_locacao`, renomeei seus atributos com aliases para seguir o padrão imposto no diagrama.

    <details><summary style="font-weight: bold;">Código</summary>

    ```SQL
    --=======================--
    --====== CONSULTAS ======--
    --=======================--

    SELECT * FROM dim_cliente   AS dcli

    SELECT * FROM dim_vendedor  AS dven

    SELECT * FROM dim_carro     AS dcar

    SELECT * FROM dim_tempo     AS dtemp

    SELECT * FROM fato_locacao  AS floc

    --=======================--
    --======= CRIAÇÃO =======--
    --=======================--

    -- Dimensão Tempo
    CREATE VIEW dim_tempo AS
    WITH RECURSIVE datas  AS (
        SELECT DATETIME('2015-01-10 00:00:00') AS datahora  -- Período inicial
        UNION ALL
        SELECT DATETIME(datahora, '+1 hour')                -- Intervalo de 1 hora
        FROM datas
        WHERE datahora < DATETIME('2023-02-18 23:00:00')    -- Período final
    )
    SELECT
        datahora                            AS DataHora,                    -- PK               
        STRFTIME('%H', datahora)            AS Hora,
        STRFTIME('%d', datahora)            AS Dia,
        CAST(STRFTIME('%w', datahora)       AS INTEGER) + 1 AS DiaSemana,   -- 1=domingo
        STRFTIME('%m', datahora)            AS Mes,
        STRFTIME('%Y', datahora)            AS Ano,
        CAST((CAST(STRFTIME('%m', datahora) AS INTEGER)+2)/3 AS INTEGER) AS Trimestre
    FROM datas;

    -- Dimensão Cliente
    CREATE VIEW dim_cliente     AS
    SELECT  idCliente           AS CodigoCliente, -- PK
            nomeCliente         AS NomeCliente,
            cidadeCliente       AS CidadeCliente,
            estadoCliente       AS EstadoCliente,
            paisCliente         AS PaisCliente
    FROM tb_Cliente;

    -- Dimensão Vendedor
    CREATE VIEW dim_vendedor    AS
    SELECT  idVendedor          AS CodigoVendedor, -- PK
            nomeVendedor        AS NomeVendedor,
            sexoVendedor        AS SexoVendedor,
            estadoVendedor      AS EstadoVendedor
    FROM tb_Vendedor;

    -- Dimensão Carro
    CREATE VIEW dim_carro       AS
    SELECT  car.idCarro         AS CodigoCarro,    -- PK
            car.chassiCarro     AS ChassiCarro,
            car.marcaCarro      AS MarcaCarro,
            car.modeloCarro     AS modeloCarro,
            car.anoCarro        AS AnoCarro,
            cb.tipoCombustivel  AS TipoCombustivel
    FROM tb_Carro car
    LEFT JOIN tb_Combustivel    AS cb
    ON cb.idCombustivel = car.idCombustivel;

    -- Dimensão Fato Locação
    CREATE VIEW fato_locacao 	AS
    SELECT
        loc.idLocacao       	AS CodigoLocacao,
        -- Métricas
        loc.qtdDiaria       	AS QuantidadeDiaria,
        loc.vlrDiaria       	AS ValorDiaria,
        loc.kmCarro         	AS QuilometragemCarro,
        -- FKs para Dimensão Tempo (DATA)
        tLoc.DataHora       	AS DataLocacao,
        tEnt.DataHora       	AS DataEntrega,
        -- Horas puxadas direto da tabela original (TIME)
        loc.horaLocacao     	AS HoraLocacao,
        loc.horaEntrega     	AS HoraEntrega,
        -- FKs das dimensões
        loc.idCliente       	AS CodigoCliente,   -- FK
        loc.idVendedor      	AS CodigoVendedor,  -- FK
        loc.idCarro         	AS CodigoCarro      -- FK
    FROM tb_Locacao loc
    -- Relação com Dimensão Tempo
    JOIN dim_tempo tLoc ON DATE(loc.dataLocacao) = DATE(tLoc.DataHora)
    JOIN dim_tempo tEnt ON DATE(loc.dataEntrega) = DATE(tEnt.DataHora);
    ```
    </details>

    <details><summary style="font-weight: bold">Criando as tabelas</summary>

    ![Evidência Criação das Views](../Evidencias/Etapa%202%20-%20Dimensional/imagens-execucao/criando_views.png)

    </details>
<br>

- Após a fase de diagramação e criação das views, foi o momento de execução e testar. Abaixo você encontrará o sucesso da execução.
    <details><summary style="font-weight: bold">Obtive esse retorno</summary>

    ![Evidência DIM Execução](../Evidencias/Etapa%202%20-%20Dimensional/imagens-execucao/evidencia2_etapa2_execucao.png)