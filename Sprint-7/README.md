# 📝 Resumo

## 🔍 Índice
- [Competências Aplicadas](#-competências-aplicadas)
- [Curso: Pyspark](#%E2%80%8D-curso-pyspark--fundamentos-análise-aws--athena--análise-serverless)
- [Exercícios](#-exercícios)
- [Evidências](#%E2%80%8D-evidências)
- [Desafio da Sprint](#-desafio-da-sprint)
- [Certificados](#-certificados)



## 🧠 Competências aplicadas
- Processamento de dados com PySpark
- Manipulação de dados com DataFrames e RDDs
- Integração com APIs (TMDB)
- Execução de aplicações em ambiente distribuído
- Uso de Docker para ambiente de dados
- Fundamentos de Big Data
- Conceitos de Analytics na AWS

## 🔶 Curso: Pyspark | Fundamentos Análise AWS | Athena | Análise Serverless
### Formação Spark com Pyspark: o Curso Completo
**<details><summary>Seção 1: Introdução</summary>**

- **O que é Spark?**  
    Uma ferramenta de Processamento de Dados (seu principal propósito não é Data Storage, como às vezes é usado na prática). Além disso, ele é distribuído em cluster, é em memória, veloz, escalável, processa dados em HDFS ou Cloud e tem suporte ao particionamento.

- **Características**  
    - Replicação e Tolerância a falha.
    - Particionamento de dados
    - Possibilidade de Distribuição em Cluster.
    - Originalmente desenvolvido na Linguagem Scala, mas pode-se utilizar Python, Java, R e SQL.

- **Spark Vs. Python, R ou Banco de Dados**  
    - Spark é necessário para processar dados, tem custo computacional (CPU, memória, rede, etc), tem arquitetura voltada a processar dados (melhor performance), porém não substitui Python, SQL ou um SGBD.

- **Componentes**  
    - Machine Learning (MLib).
    - Spark SQL.
    - Processamento em Streaming (processa dados estruturados e novos registros adicionados ao final da tabela).
    - Processamento de Grafos (GraphX) (Spark constrói grafos acíclicos dirigidos)
    - Motor de execução do Spark é o Tungsten (o foco é a eficiência da CPU).
    - Job: tarefa a ser executada
    - Stage: divisão do job
    - Task: Menor unidade de trabalho. Uma por núclo e por partição.

- **Estrutura**  
    - `Driver` inicializa SparkSession, solicita recursos computacionais do Cluster Manager, transforma as operações em DAGs, distribui estas pelos executers.
    - `Manager` gerencia os recursos do cluster. Quatro formas de gerenciar recursos do cluster: built-in standalone, YARN, Mesos e Kubernetes.
    - `Executer` roda em cada nó do cluster executando as tarefas.

- **Transformações e Ações**  
    O principal elemento de dados do Spark é um **data frame**. Data Frame é imutável, trazendo intolerância a falha. Uma transformação gera um novo data frame e o processamento de transformação de fato só ocorre quando há uma Ação: Lazy Evaluation.  

    Elas podem ser de dois tipos: 
    - `Narrow`: os dados necessários estão em uma mesma partição.
    - `Wide `: os dados necessários estão em mais de uma partição.

- **Formatos de Big Data**  
    - Armazéns de Dados Clássicos: Formatos proprietários
    - Armazéns de Dados Modernos: Formatos abertos (qualquer ferramenta pode consultar ou criar esse formato, sem a necessidade de um driver).  
    Armazéns de dados modernos tendem a armazenar dados em formatos "desacoplados" de ferramentas e abertos, seus formatos são binários e compactados. Também suportam Schema (características dos dados já ficam armazenados no próprio dado), podendo serem particionados entre discos.

    - **Formatos:**  
    Informações com muitos atributos e mais escrita, o mais apropriado é linha. Quando há informações com menos atributos e mais leitura, o apropriado é coluna.
        - Parquet: colunar, padrão do spark
        - ORC: colunar, padrão do Hive
        - Avro: linha

- **Qual escolher?**  
    Em geral ORC é mais eficiente na criação (escrita) e na compressão.  
    Parquet tem melhor performance na consulta (leitura).  
    O ideal mesmo é fazer um benchmark.
</details>

**<details><summary>Seção 2: Primeiros Passos</summary>**

Após a instalação da VM Ubuntu e do Spark, foi feita a instalação dentro da VM do interpretador Python3 e as bibliotecas Pandas e Numpy. Além disso foi feita a instalação do aplicativo Putty para podermos acessar o Ubuntu via terminal do Windows por SSH.
</details>

**<details><summary>Seção 3: Dataframes e RDDs</summary>**

As estruturas de mais alto nível do Spark são as estruturas de Dataset e Dataframe. São semelhantes a uma tabela de banco de dados e são compatíveis com objetos Dataframe do R e Python.
- Dataset são disponíveis apenas em Java e Scala.

<details><summary>RDD (Resilient Distributed Datasets)</summary>

- **Suas características**
    - Estrutura básica de baixo nível
    - Mais complexo e verboso, porém mais flexível
    - Dados "imutáveis", distribuídos pelo cluster
    - Em memória
    - Pode ser persistindo em disco
    - Tolerante a falha
    - Operações sobre um RDD criam um novo RDD
    - Otimização dificil pelo Spark

- **Funções**  
    - `sc.parallelize()`: converte uma coleção local do driver em um RDD.
    - `.take()`: pega os 5 primeiros elementos.
    - `.top(5)`: mostra os 5 maiores.
    - `.collect()`: mostra todos os dados, no entanto em algumas situações não é recomendado.
    - `numeros.count()`: conta a quantidade de elementos.
    - `.mean()`: média dos valores.
    - `.sum()`: soma os valores.
    - `.min()`: menor valor.
    - `.max()`: maior valor.
    - `.stdev()`: desvio padrão dos valores.
    - `.filter()`: filtra os dados.
    - `.sample`: cria uma amostra.
    - `.map()`: aplica a função lambda à todos os elementos.
</details>

<details><summary>DataFrames</summary>

- **Suas características**  
    - É uma tabela com linhas e colunas.
    - Dados imutáveis.
    - Com Schema conhecido (você pode deixar para o Spark inferir a partir de parte dos dados ou definir manualmente o schema).
    - Linhagem preservada.
    - Colunas podem ter tipos diferentes.
    - Existem análises comuns: Agrupar, ordenar, filtrar.
    - Spark pode otimizar estas análises através de planos de execução.

- **Funções**  
    - `.createDataFrame()`: cria o dataframe.
    - `.show()`: mostra o dataframe.
    - `.groupBy()`: agrupa pelo tipo selecionado.
    - `.select()`: seleciona uma coluna.
    - `.schema`
    - `.columns`: mostra as colunas.
    - `spark.read.load(path="caminho/do/arquivo", format="formato", **opções)`: spark faz a  inferência dos dados. (forma genérica)
    - `spark.read.format("formato").load("caminho/arquivo.formato")`: inferência dos dados também (forma genérica também).
    - `spark.read.csv("caminho/arquivo.csv")`: carrega os dados também (forma mais específica).
    - `.write.format("").save("caminho/do/arquivo` exporta os dados no formato que escolher.
</details>
</details>

**<details><summary>Seção 4: Spark SQL</summary>**

- **Tabela**  
    É um tipo de objeto tabular que reside em um banco de dados e é persistente. Ela pode ser gerenciada e consultada utilizando SQL e é totalmente interoperável com DataFrame.  
    Pode-se transformar um Dataframe que importar em tabela.  
    As `tabelas gerenciadas` o Spark gerencia dados e metadados, são armazenadas no warehouse do Spark e se excluirmos, tudo é apagado (dados e metadados)  
    As ` tabelas não gerenciadas (external)` o Spark apenas gerencia metadados. Nós informamos onde a tabela está (arquivo, por exemplo orc) e se excluírmos, o Spark só exclui os metadados, permanecendo assim os dados onde estavam.

- **Views**  
    Mesmo conceito de bancos de dados relacionais. São como um "alias" para uma tabela (por exemplo "venda_rs" pode mostrar vendas do estado já com filtro aplicado). Não contém dados.  
    As `Views Globais` são visiveis em todas as sessões.  
    As `Views de Sessão` são visíveis apenas na própria sessão.
</details>

**<details><summary>Seção 6: Criando Aplicações</summary>**

- Argumentos na linha de comando:
    - O primeiro é sempre o nome do aplicativo
    - Podemos definir opções e valores
    - Podemos ler as opções e os respectivos valores, por exemplo:  
    `programa -t [formato] -i [csv de entrada] -o [diretório de saída]`
</details>

**<details><summary>Seção 9: Otimização</summary>**

- **Particionamento e Bucketing**  
    Por padrão os dados são particionados de acordo com o número de núcleos, onde cada partição fica em um nó e tem uma task, deeles dependem de vários fatores e configurçaões.  
    É possível particionar explicitamente em disco (`partitionBy`) ou em memória `repartition() or coalesce()`.  
    `Shuffle` é uma redistribuição de dados entre partições.  
    `Bucketing` é semelhante a particionamento, porém com número fixo de partições. Ideal para coluna com alta cardinalidade (muitos valores únicos). Pode ser usado com conjunto com Particionamento.
</details>

### 📊 Curso AWS Skillbuilder: Fundamentals of Analytics on AWS

**<details><summary>Conceitos de Analytics</summary>**

`Analytics` é o processo de usar técnicas e ferramentas especializadas para encontrar um novo vlaor em dados brutos. Ajuda empresas a decidir onde e quando lançar novos produtos, oferecer descontos e expandir para novos mercados. Sem isso, muitas decisões seriam tomadas em intuição e sorte. 
`Análise de Dados` é a prática de interpretar dados que leva à tomada de decisões significativas.

- **Tipos e técnicas de Analytics**  
    - `Analytics Descritiva`: Usa técnicas de visualização de dados, como gráficos de pizza, de barras, de linhas, narrativas geradas e tabelas.
    - `Analytics Diagnóstica`: Ajuda a responder por algo que aconteceu, usando técnicas como:
        - Detalhamento: visão geral dos dados até obter uma visão detalhada no mesmo conjunto de dados.
        - Descoberta de dados: um processo para coletar, catalogar e classificar dados de diferentes DBs para fins de analytics.
        - Mineração de Dados: uso de analytics em grande conjunto de dados para descobrir informações significativas.
        - Correlações: uma medida entre duas variáveis que mostra o quão intimamente relacionadas elas estão sem declarar uma relação de causa e efeito.
    - `Analytics Preditiva`: Ajuda a responder o que pode acontecer no futuro. Usando técnicas como:
        - Machine Learning
        - Previsão
        - Correspondência de padrões
        - Modelagem preditiva
    - `Analytics Prescritiva`: Recomenda ações para o resultado previsto. Usando técnicas como:
        - Análise de gráfico
        - Simulação
        - Processamento de eventos complexos
        - Redes neurais
        - Mecanismos de recomendação

- **Machine Learning**  
    - `Inteligência Artificial`: amplo ramo da ciência da computação envolvido na construção de máquinas inteligentes que podem executar tarefas que exigem inteligência humana.
    - `Modelo de Machine Learning`: programa projeto para encontrar padrões em um conjunto de dados não analisado.
    - `Algoritmo de ML`: programa que ajuda os computadores a entender padrões ocultos nos dados, fazer previsões sobre os dados e recomendar ações a serem tomadas.

    Machine Learning é um subconjunto da IA. Os computadores utilizam ML para aprender com dados e fazer previsões com base neles. Os Modelos podem prever probabilidades futuras e oferecer um curso de ação. (Analytics Preditiva e Prescritiva).  
    Por meio do treinamento os modelos se tornam mais precisos e os dados são executados nas aplicações várias vezes usando regras e restrições, refinando a capacidade de fazer recomendações precisas.  
    Os algoritmos de ML podem analisar grandes volumes de dados mais rapidamente que humanos. Eles podem ser criados para **identificar tendências, correlações e anomalias**. O ML automatiza o processo de extração das informações e padrões dos dados, economizando tempo e esforço.

    Na AWS pode-se criar uma carga de trabalho baseada em ML, escolhendo entre três níveis diferentes de serviços:
    - `Serviços de IA da AWS`: fornecem aos Devs inteligência de IA para integração com aplicações e workflows. Esses serviços usam a mesma tecnologia de Deep Learning que alimenta os serviços da Amazon.com e de ML da Amazon.
    - `Serviços de ML`: qualquer desenvolvedor pode facilmente acelerar a inovação de ML com ferramentas de ML com propósito específico, otimizadas para aplicações de ML.
    - `Frameworks e infraestrutura de ML`: permite criar as próprias ferramentas e workflows para criar, treinar, ajustar e implantar modelos.

- **Gen AI na AWS**  
    Um tipo de modelo de ML que cria novos conteúdos e ideias a partir das solicitações do usuário. Além de dados, também gera conteúdo como conversas, histórias, imagens, vídeos e músicas.

- **Amazon Q Developer**  
    Serviço de geração de código que analisa seu código e comentários enquanto você escreve código na IDE. Utiliza NLP para entender os comentários no código, gerando funções completas e blocos de código que se alinham com as descrições.

- **Os 5 Vs do Big Data**  
    Refere-se às caracterísitcas fundamentais que definem o gerenciamento de grandes conjuntos de dados:
    - `Volume`: tamanho total dos dados recebidos.
    - `Variedade`: quantidade de diferentes fontes e os tipos de fontes que a solução usará.
    - `Velocidade`: velocidade com que os dados chegam e avançam para serem processados.
    - `Veracidade`: grau de exatidão, precisão e confiança dos dados. Isso depende da integridade e credibilidade dos dados.
    - `Valor`: capacidade de extrair informações significativas dos dados que foram armazenados e analisados.

    Os 5 desafios:
    <details><summary>Volume</summary>

    O grande volume de dados dificulta o gerenciamento eficiente por parte dos sistemas de armazenaemntos tradicionais. Toda empresa com dados precisa de uma grande quantidade de capacidade de computação e armazenamento.  
    Exemplos de fontes de dados para ingestão e armazenamento:
    - `Dados transacionais` (informações de clientes, compras de produtos on-line, contratos de serviço)
    - `Dados temporários` (movimentos feitos em um video game online, cache do navegador da internet e etc.)
    - `Objetos` (imagens, mensagens de email, arquivos de texto, conteúdo da internet, mensagens, vídeos)
    </details>

    <details><summary>Variedade</summary>

    as fontes de dados podem vir de dentro e de fora de uma organização. A variedade dos dados diz respeito à forma como a fonte de dados organiza vários tipos de dados.  

    **Tipos de Fontes de Dados**  
    - `Dados Estruturados` (CRM, formulários online, registros de rede, sistemas de reserva)
    - `Dados semiestruturados` (CSV, JSON, XML)
    - `Dados não estruturados` (emails, PDFs, fotos, vídeos, documentos, dados de clickstream)
    
    Os dados estruturados e semiestruturados são armazenados em SGDBs e os Não Estruturados em Data Lakes ou soluções de armazenamento de objetos.

    **Métodos de Armazenamento**
    - `Estruturado`: bancos de dados relacionais armazenam dados em tabelas relacionadas entre si, com o objetivo de armazenamento otimizado.
    - `Semiestruturados (NoSQL)`: bancos de dados não relacionais são criados para armazenar dados semiestruturados para coleta e recuperação rápidas. Armazenam dados como uma coleção de documentos ou pares de chave-valor.
    
    **Sistemas OLTP e OLAP**  
    Em bancos de dados existem dois métodos primários para organizar informações: `Processamento de Transação Online (OLTP)` e `Processamento Analítico On-line (OLAP)`.  
    - OLTP gerencia transações operacionais diárias e rápidas
    - OLAP analisa grandes volumes de dados históricos para suporte à decisão  
    
    Sendo necessários dois sistemas diferentes, com base na forma que os recursos que suportam o banco de dados estão sendo usados: armazenar e recuperar dados.  
    - Adição de dados no BD é chamada de Operação de Gravação;
    - Consulta de dados é chamada de Operação de Leitura;  

    Bancos de dados menores toleram operações simultâneas de gravação e leitura, no entanto, bancos grandes tendem a ter apenas a opção de sacrificar o desempenho de leitura para permitir operações de gravação ou vice-versa.  
    Por isso a solução é usar um banco de dados `OLTP otimizado para operações de gravação` e `OLAP para operações de leitura`.  
    Na prática, os dados são gravados no BD OLTP com uma frequência muito alta, os registros desse sistema são copiados para um sistema OLAP de forma agendada.

    **Armazenamentos de dados com Propósito Específico:**  
    |Banco de Dados | Descrição |
    |:-------------:|:---------:|
    |Amazon Aurora  | SGDB relacional sem servidor, alto desempenho, alta disponibilidade, escalável e proprietário com compatibilidade com MySQL e PostgreSQL|
    | Amazon RDS    | Serviço gerenciado de BD relacional na nuvem, com várias opções de mecanismo de banco de dados.|
    | Amazon Redshift | Armazenamento de dados baseado na nuvem com ML, oferece melhor custo-benefício em qualquer escala |
    | Amazon DynamoDB | BD NoSQL rápido, flexível e altamente escalável |
    | Amazon ElastiCache | Serviço de cache de dados totalmente gerenciado, econômico e altamente escalável para desempenho em tempo real. |
    | Amazon MemoryDB para Redis | BD com memória durável e compatível com Redis para desempenho ultrarrápido |
    | Amazon DocumentDB | BD de documentos JSON totalmente gerenciado e escalável compatível com MongoDB|
    | Amazon Keyspaces | Serviço BD gerenciado, sem servidor, de alta disponibilidade, escalável e compatível com Apache Cassandra|
    |Amazon Neptune | BD gráfico sem servidor, escalável e de alta disponibilidade|
    | Amazon Timestream | BD de série temporal rápido, escalável e sem servidor|
    | Amazon Quantum Ledger Database (QLDB) | BD ledger totalmente gerenciado e verificável com criptografia|
    | AWS DMS | Serviço gerenciado e automatizado de migração e replicação para mover cargas de trabalho de BD e analytics para a AWS com mínimo de tempo de inatividade e zero perda de dados.|
    </details>

    <details><summary>Velocidade</summary>

    Existem quatro velocidades de processamento de dados:
    - `Agendado`: representa os dados que são processados em um volume muito grande com agendamento regular. Ex: 1x por semana, 1x por dia. Geralmente é a mesma quantidade de dados com cada carga, tornando esses workloads previsíveis.
    - `Periódico`: é um lote de dados processados em momentos irregulares. Esses workloads geralmente são executados quando determinada quantidade de dados é coletada. Isso pode torná-los imprevisíveis e difíceis de planejar.
    - `Quase em tempo real`: representa dados de streaming que são processados em pequenos lotes individuais, aos quais são constantemente coletados e processados em minutos após a geração dos dados.
    - `Em tempo real`: representa dados de streaming processados em lotes individuais muito pequenos. São constantemente processados e coletados em milissegundos após a geração de dados.

    Há dois tipos de processamento de dados: `em lote e de streams`.
    - Processamento em Lote é usado quando há muitos dados para processra e isso precisa ser feito em intervalos. Por exemplo quando são processados seguindo cronogramas ou quando um determinado volume é atingido. Geralmente é feito em conjuntos de dados, como logs de servidores, dados financeiros, relatórios de fraudes e resumos de clickstream.
    - Processamento de Streams processa dados gerados de forma contínua. É usado, por exemplo, para feedback em tempo real ou informações contínuas. 
    </details>


    <details><summary>Veracidade</summary>

    - `ETL`: Garantir que os dados tenham acurácia, precisão e detalhamento necessários, reunindo-os de diferentes fontes para uma visão completa e criando conjuntos de dados com propósito específico. (Extração, Transformação e Carregamento dos dados)
    - `ELT`: O processo de ELT, em comparação com ETL, requer mais definição no início. Analytics deve estar presente desde o início para definir tipos, as estruturas e relacionamentos dos dados de destino. Toda a limpeza, transformação e enriquecimento de dados ocorrem dentro do data warehouse. (Extração, Carregamento - em um data warehouse ou data lake - e Transformação dos dados)
    </details>

    <details><summary>Veracidade</summary>

    **Consulta e Geração de Relatórios**  
    Relatórios analíticos são usados para transformar dados em informações úteis que capacitam as organizações na tomada de decisões, otimizam processos e alcançam objetivos estratégicos.  
    Necessário seguir algumas etapas para ter êxito:
    - Coletar os dados, os fatos, os itens de ação e as conclusões
    - Identificar o público, as expectativas dele e o método adequado de entrega
    - Identificar os estilos de visualização e o estilo do relatório que melhor atenderão às necessidades do público
    - Criar os relatórios e painéis

    **Visualização de Dados**  
    Com dados visuais bem construídos, podemos descrever os dados, explicar por que são importantes e como avançar com as informações fornecidads. Para criar um visual eficaz, é necessário identificar os tipos de analytics que atendem às necessidades da solicitação de analytics.  
    Existem três tipos principais de relatórios visuais:
    - Relatórios estáticos
    - Relatórios interativos
    - Painéis
    </details>
</details>

**<details><summary>Serviços da AWS para Analytics</summary>**

<details><summary>Serviços da AWS para Variedade</summary>

- **Amazon RDS**  
    O Amazon RDS facilita a migração dos bancos de dados on-premises para a nuvem quando uma organização deseja migrar, facilitando a configuração, a operação e o scaling de um banco de dados relacional na nuvem. Ele resolve desafios de variedade de dados em termos de fornecedores, escalabilidade e desempenho. O RDS suporta muitos SGBDs como Amazon Aurora, MySQL, PostgreSQL, MariaDB, Oracle e SQL Server.  
    O serviço oferece capacidade redimensionável e econômica, enquanto automatiza tarefas administrativas demoradas, além de simplificar a replicação para aumentar a disponibilidade do BD e a durabilidade dos dados. Serve também para escalar, além das limitações de capacidade de uma instância, os workloads de BDs de leitura intensiva. Tem uma indexação baseada em linhas para alcançar desempenho certo para workloads transacionais.

- **Amazon Redshift**  
    Resolve desafios de variedade de dados, quando empresas precisam consultar e analisar dados em todos os departamentos. Ele é um serviço de data warehouse baseado na nuvem na AWS, onde analisa dados estruturados e semiestruturados, data lakes e data warehouses para oferecer melhor relação preço/desempenho em qualquer escala. 

- **Amazon DynamoDB**  
    Resolve vários desafios de bancos de dados NoSQL, sendo um serviço totalmente gerenciado para armazenamento de dados, fornecendo desempenho rápido e previsíviel com escalabilidade contínua.

- **Amazon OpenSearch Service**  
    Facilita analytics interativa de logs, monitoramento de aplicações em tempo real e pesquisa em sites. É um serviço gerenciado da AWS para executar e escalar clusters do OpenSearch, para as empresas não se preocuparem com o gerenciamento, monitoramento e manutenção da infraestrutura, nem desenvolver uma profunda experiência em operação de clusters do OpenSearch.  
    O OpenSearch é um conjunto distribuído e de código aberto de pesquisa e analytics para uma ampla gama de casos. Ele fornece um sistema rápido e altamente escalável para explorar e visualizar dados, com painéis dashboards fáceis de usar. Suporta a integração com dados de streaming de buckets do Amazon S3, Kinesis Data Streams e DynamoDB Streams.
</details>


<details><summary>Serviços da AWS para Velocidade</summary>

Existem vários serviços também para ajudar a lidar com a velocidade dos fluxos de dados:

- **Amazon EMR**  
    Fornece uma plataforma de big data escalável e gerenciada que processa e analisa com eficiência grandes volumes de dados em velocidades variáveis.
    Ele simplifica o processamento de grandes conjuntos de dados e gerencia a infraestrutura.
    - Execução de aplicações de big data e análises em escala de petabytes de forma rápida.
    - Menos da metade do custo das soluções on-premises.
    - Integração perfeita com Amazon SageMaker
    - Execução de tarefas de ML em grandes conjuntos de dados.
    - Usa frameworks de big data de código aberto (Spark, Hadoop, HBase, Hive, Hudi, Presto) para distribuir tarefas de processamento de dados
    - Usa recursos de processamento paralelo para garantir que dados possam ser ingeridos, transformados e analisados de forma rápida.

- **Amazon MSK**
    Ajuda a processar fluxos de dados de alta velocidade com conveniência e confiabilidade. É um serviço totalmente gerenciado que ajuda a criar e executar aplicações que usam Apache Kafka para streaming em tempo real e arquiteturas orientadas por eventos.

- **Amazon Kinesis**  
    Plataforma totalmente gerenciada que resolve os desafios de velocidade ao ingerir, processar e analisar dados em tempo real, à medida que eles são gerados. Esses dados de alta velocidade podem ser usados para ML, análises em tempo real e outras aplicações.

- **AWS Lambda**  
    Serviço computacional sem servidor que ajuda a enfrentar os desafios de velocidade com processamento de dados em tempo real e orientado por eventos. O Lambda executa código em resposta a eventos, como alterações nos dados em um bucket do Amazon S3 ou atualizações em uma tabela do DynamoDB. Eventos e mudanças nos dados podem gerar respostas rápidas sem a necessidade de gerenciar a infraestrutura.  
    O Lambda processa dados em tempo real, escala automaticamente para diferentes velocidades de dados e se integra a outros serviços da AWS pra criar aplicações e canais robustos de processamento de dados. Com ele, não é necessário invocar ou configurar servidores, em vez disso, eventos iniciam um fluxo de trabalho, como a ingestão em uma instância do Amazon DynamoDB. Nesse fluxo, os dados podem ser produzidos para análise, consulta e outros usos de negócios.
</details>

<details><summary>Serviços da AWS para Veracidade</summary>

- **Amazon EMR**  
Ajuda com desafios de qualidade, precisão e integridade dos dados. Fornece uma plataforma robusta de coleta e processamento de dados para analisar grandes quantidades de dados. Retira a preocupação com o gerenciamento da infraestrutura.  
É uma abordagem prática para criar pipeline de dados e requer que a sua equipe tenha um forte conhecimento técnico.

- **Amazon Glue**  
    Ajuda com desafios de qualidade e integridade. É um serviço de ETL gerenciado e de integração de dados sem servidor. Esse serviço oferece uma experiência mais simplificada do que o EMR.  
    Facilita a limpeza e a normalização de dados diretamente de DL, DW e BDs.
    Ele pode consumir dados de fontes de streaming, limpá-los e transformá-los em tempo real, além de compartilhá-los para análise em segundos no armazenamento escolhido.  
    Possível processar dados de eventos, como streams de eventos IoT, clickstreams e logs de rede, além de executar operações complexas de análise e ML.  
    Também pode ser usado como um metastore para os dados finais transformados usando o Glue Data Catalog ou gerenciar a qualidade dos dados em conjuntos de dados com o Glue Data Quality.

- **AWS Glue DataBrew**  
    Uma ferramenta visual para preparar dados. Ele permite que analistas e cientistas de dados limpem, normalizem e transformem dados sem precisar escrever código, usando mais de 250 transformações prontas. Ele se conecta diretamente com serviços Amazon como S3, Redshift, Lake Formation, e funciona no modelo pagamento por uso.

- **Amazon DataZone**  
    É voltado para governança e gerenciamento de dados. Permite catalogar, descobrir, compartilhar e controlar o acesso a dados dentro da organização, aplicando políticas de segurança e conformidade em larga escala. Facilita colaboração entre equipes e integra serviços como Redshift, Glue, Athena, IAM.
</details>

<details><summary>Serviços da AWS para Valor</summary>

- **Amazon QuickSight**  
    Ferramenta de BI da AWS para criar dashboards, relatórios e visualizações interativas. Conecta em várias fontes como S3, Redshift, RDS e Athena, permitindo preparar dados antes da visualização e ainda integrar previsões de ML nos painéis. A ideia é transformar dados em insights visuais fáceis de compartilhar.

- **Amazon SageMaker**  
    Plataforma completa de ML da AWS. Permite preparar dados, criar, treinar, ajustar e implantar modelos de ML. Oferece monitoramento de desempenho e deploy escalável via endpoints. É a ferramenta para construir e colocar modelos preditivos em produção. A solução é ótima para organizações aproveitarem o poder do ML e obter informações orientadas por dados.

- **Amazon SageMaker JumpStart**  
    Um hub dentro do SageMaker com modelos prontos, algoritmos integrados e soluções pré-construídas. Ele acelera o desenvolvimento porque pode-se testar, personalizar e implantar modelos à existentes sem começar do zero.

- **Amazon Bedrock**  
    Focado em IA Generativa. Oferece acesso, via API pública, a modelos de base de empresas como Anthropic e Meta, permitindo criar aplicações com IA generativa sem precsiar gerenciar infraestrutura. É totalmente gerenciado e voltado para escalar soluções de IA.

- **Amazon Athena**  
    Um serviço serverless para consultar dados direto no S3 usando SQL. Ele é ideal para análises exploratórias e consultas rápidas, sem precisar configurar servidor ou banco. Integra com outros serviços AWS e paga só pelo o que consultar.
</details>
</details>

## Data & Analytics
### Apache Hadoop
O Hadoop é um framework Open Source, como o Spark, que permite gerenciar e processar big data com eficiência em um ambiente de computação distribuído.  
Ele consiste em 4 módulos principais:
<details><summary>Hadoop Distributed File System (HDFS)</summary>

- Sistema de arquivos distribuído do Hadoop
- Funciona de forma parecida com um sistema de arquivos local, mas distribuído
- Utiliza conceito semelhante a `object storage`
- Armazena dados como objetos de tamanho variável
- Tem alta durabilidade e disponibilidade, além de replicação de dados, elasticidade e escalabilidade, sendo esta praticamente ilimitada

**Vantagens**:
- Melhor desempenho para grandes volumes
- Melhor que sistemas de arquivos tradicionais nesse contexto
- Excelente escalabilidade
- Permite expandir de uma única máquina para milhares
- Pode rodar em hardware comum
</details>

<details><summary>Yet Another Resource Negotiatior (YARN)</summary>

- Facilita tarefas agendadas
- Gerenciamento completo e monitoramento de nós de cluster, entre outros recursos.
</details>

<details><summary>Map Reduce</summary>

- Módulo que ajuda os programas a realiazr computação paralela de dados
- O MAP Converte os dados de entrada em pares chave-valor
- O REDUCE consome a entrada, agrega-a e produz o resultado
- Abstrai as complexidades do trabalho com dados distribuidos, evitando problemas de compartilhamento de informações

**Etapas do Map Reduce**  
- Map: recebe os dados de entrada como pares chave-valor. Codificado pelo dev.
- Shuffle: organiza os resultados do map, agrupando valores por chave para o reduce.
- Reduce: processa os dados agrupados e retorna novos pares chave/valor. Também codificado pelo desenvolvedor.

</details>

<details><summary>Hadoop Common</summary>

- Usa bibliotecas Java que são padrões em todos os outros módulos.
</details><br>

**Ecossistema do Hadoop**  
O ecossistema Hadoop é formado pelos 4 módulos principais e ferramentas complementares. Cada ferramenta resolve necessidades específicas, criando uma infraestrutura completa para armazenamento, processamento, acesso e gerenciamento de grandes volumes de dados.
- Componentes Principais: HDFS e MapReduce.
- Ferramentas de Aesso aos dados: Pig, Hive, Avro, Mahout (facilitam análise e consultas, oferecendo linguagens semelhantes ao SQL).
- Ferramentas de gerenciamento: ZooKeeper, Flume, Chukwa (melhoram a administração e interação com aplicações).

<details><summary>Arquitetura dos Componentes Básicos</summary>

Para que o Hadoop funcione, é necessário cinco processos: `NameNode`, `DataNode`, `SecondaryNameNode`, `JobTracker` e `TaskTracker`. Os três primeiros são integrantes do modelo MapReduce e os dois últimos do HDFS. 
NameNode, JobTracker e SecondaryNameNode são únicos para toda aplicação, enquanto os demais são instanciados para cada máquina do cluster.

- `NameNode`: Também conhecido como "nó mestre". Gerencia os arquivos armazenados no HDFS, mantém uma tabela de metadados com informações sobre quais DataNodes guardam cada bloco, tem funções de mapear localização, dividir arquivos em blocos, encaminhar blocos e controlar réplicas. Mantém dados em memória para desempenho e fica localizado no nó mestre junto com o JobTracker
- `Datanode`: Também conhecido como "nós escravos". É responsável por armazenar o conteúdo dos arquivos, existe várias instâncias em um cluster Hadoop, eles armazenam múltiplos blocos, inclusive de arquivos diferentes e precisam se reportar constantemente ao NameNode, informando operações realizadas.

**Arquitetura Master-Slave do MapReduce**  
- Jobtracker: coordena a execução das tarefas Map e Reduce. Monitora e redistribui em caso de falhas
- TasktTracker: executa as tarefas atribuidas. Cada nó escravo possui um ou mais TaskTrackers.
- SecondaryNameNode: auxilia o NameNode com pontos de checagem e recuperação em caso de falha.
</details><br>

### Apache Spark

Componentes do Spark:  
- SparkSQL + Dataframes
- Spark Streamming
- GraphX
- MLlib
- Spark-Core

Arquitetura:  
- Driver Program (aplicação principal que gerencia a criação e é quem executará o processamento definido).
- Cluster Manager (componente opcional, apenas necessário se Spark for executado de forma distribuída. Responsável por administrar as máquinas que serão utilizadas como workers).
- Workers (máquinas que executarão as tarefas enviadas pelo Driver Program).

Oferece suporte a varios gerenciadores de cluster como:
- Standalone
- Apache Mesos
- Hadoop YARN
- Kubernetes

O Apache Spark atinge alto desempenho para dados em batch e streaming, usando um agendador DAG de última geração, um otimizador de consulta e mecanismo de execução física, chegando a ser até 100x mais rápido que  o Hadoop.


### Resumo 
**Apache Hadoop é bom para**:
- Processamento linear de grandes conjuntos de dados, onde MapReduce permite o processamento paralelo de grandes quantidades. Ele divide um grande fragmento em partes menores para serem processadas separadamente em diferentes nós de dados e reúne automaticamente os resultados nos vários nós para retornar um único resultado. Caso o conjunto de dados resultante seja maior que a RAM disponível, o Hadoop MapReduce pode superar o Spark.
- Solução econômica, se não houver resultados imediatos. Considera-se MapReduce uma boa solução se a velocidade de processamento não for crítica. Por exemplo, se o processamento de dados puder ser feito durante a noite, faz sentido considerar o uso do MapReduce do Hadoop.

**Spark é bom para**:
- Processamento rápido de dados. O processamento é mais rapido que o Hadoop MapReduce, até 100 vezes para dados na RAM e até 50 vezes para os armazenados.
- Processamento iterativo (os RDDs resilientes do Spark permitem  várias operações de mapa na memória enquanto no MapReduce do Hadoop tem que gravar resultados provisórios em um disco)
- Processamento quase em tempo real. Se necessitar de insights imediatos.
- Machine Learning. Ele possui biblioteca MLib, enquanto o hadoop precisa que um terceiro forneça. O MLib tem algoritmos prontos que são executados na memória.
- Juntando conjunto de dados.

# ✍ Exercícios

1. <details><summary><a href="./Exercicios/contador-de-palavras/">Exercício 1 - Contador de Palavras</a></summary>

    Neste exercício, foi solicitado para criarmos um arquivo dockerfile, na qual faria a cópia do arquivo README direto para dentro do container. Nos logs do container criado, aparece um link no terminal, que leva direto ao Jupyter Lab, ao qual devemos entrar em um executor do Python3, rodando assim o script que faria a contagem de palavras do README.
    O principal responsável por isso é o Pyspark.  
    Além disso, para facilitar a documentação e organização do código
    ```dockerfile
    FROM jupyter/all-spark-notebook

    WORKDIR /home/jovyan

    COPY 'Sprint-7/README.md' /home/jovyan/README.md
    ```
    Execução do Dockerfile:
    ```bash
    # Montar a imagem
    docker build -f Sprint-7/Exercicios/contador-de-palavras/Dockerfile -t contar_palavras .

    # -f é o caminho do Dockerfile
    # -t é o nome da imagem
    # . é a raiz do projeto

    # Rodar o container baseado na imagem do jupyter/all-spark-notebook
    docker run -p 8888:8888 -it contar_palavras

    # Clique na linha no terminal que diz:
    http://127.0.0.1:8888/lab?token=...

    # Crie um Terminal ou um arquivo .ipynb no Jupyter Lab    
    ```
    
    Script Python:
    ```py
    from pyspark.sql import SparkSession
    spark = SparkSession                        \
                .builder                        \
                .appName("ContadorPalavras")    \
                .getOrCreate()
    textFile = spark.sparkContext.textFile("README.md")
    words = textFile.flatMap(lambda line: line.split())
    counts = words.map(lambda word: (word,1)).reduceByKey(lambda a, b: a + b)
    result = counts.collect()
    print(result)
    ```
</details>

2. <details><summary><a href="./Exercicios/tmdb/">Exercício 2 - Conexão à API do TMDB</a></summary>

    Neste exercício foi apenas solicitado que fizéssemos a conta no TMDB e testássemos a conexão com a API do TMDB utilizando um script pré-pronto.

    ```py
    import requests
    import pandas as pd
    from IPython.display import display

    api_key = "36211654b2fd075c9f34f5f7b7827f9e"

    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&amp;language=pt-BR"

    response = requests.get(url)
    data = response.json()
    filmes = []

    for movie in data['results']:
        df = {
            'Titulo': movie['title'],
            'Data de lançamento': movie['release_date'],
            'Visão geral': movie['overview'],
            'Votos': movie['vote_count'],
            'Média de votos': movie['vote_average']
            }
        
        filmes.append(df)

    df = pd.DataFrame(filmes)
    display(df)
    ```
</details>

# 👁‍🗨 Evidências
Como os exercícios foram bem simples, não achei necessário registrar apenas o terminal executado.

# 🎯 Desafio da Sprint
O desenvolvimento do desafio da sprint e seus respectivos arquivos relacionados encontram-se em sua pasta, assim como seu README que fora usado para dissertar sobre os passos executados e resultados.
O Readme do Desafio foi dividido em etapas, seguindo a lógica proposta pela Compass e tais quais apresentam e explicam as resoluções utilizadas e os resultados obtidos:
- 📁[Pasta do Desafio](../Sprint-7/Desafio/)
- 📝[README do Desafio](../Sprint-7/Desafio/README.md)
    
# ✅ Certificados

### AWS
[Certificado: Fundamentals of Analytics](./Certificados/aws%20Fundamentals%20of%20Analytics%20on%20AWS%20-%20Part%201.pdf)

[Certificado: Amazon Athena](./Certificados/aws%20introduction%20to%20amazon%20athena.pdf)

[Certificado: Serverless Analytics](./Certificados/aws%20serverless%20analytics.pdf)