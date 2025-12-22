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