-- concessionaria_normalizada.db
-- sqlite
PRAGMA foreign_keys = ON;

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