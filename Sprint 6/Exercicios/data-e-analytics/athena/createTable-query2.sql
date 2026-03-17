CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.dados_pessoas (
    Nome STRING,
    Sexo CHAR(1),
    Total INTEGER,
    Ano INTEGER
    ) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = ',',
    'field.delim' = ','
    )
LOCATION 's3://exercicio-s3-jocimar.com/dados/'
TBLPROPERTIES ('skip.header.line.count'='1');