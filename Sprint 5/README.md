# 📝 Resumo
 
## 🔍 Índice
- [Competências Aplicadas](#-competências-aplicadas)
- [Curso: Docker para Desenvolvedores (com Docker Swarm e Kubernetes)](#%E2%80%8D-curso-docker-para-desenvolvedores-com-docker-swarm-e-kubernetes)
- [Exercícios](#-exercícios)
- [Evidências](#%E2%80%8D-evidências)
- [Desafio da Sprint](#-desafio-da-sprint)
- [Certificados](#-certificados)



## 🧠 Competências aplicadas
- Containerização de aplicações
- Criação e otimização de imagens Docker
- Gerenciamento de containers
- Persistência de dados com volumes
- Configuração e gerenciamento de redes Docker
- Orquestração de múltiplos containers com Docker Compose
- Uso de YAML para configuração declarativa
- Orquestração de containers com Docker Swarm
- Orquestração de containers com Kubernetes
- Arquitetura escalável (horizontal scaling)
- Boas práticas de DevOps
- Manipulação de padrões de texto com REGEX em Python

## 👨‍🔬 Curso: Docker para Desenvolvedores (com Docker Swarm e Kubernetes)
### Seção 1: Introduction - Docker
- **O que é Docker?**  
    Docker é um software que <u>reduz a complexidade de setup</u> de aplicações, onde configuramos containers, que são como servidores para rodar nossas aplicações. Com facilidade, podemos criar ambientes independentes e que funcionam em diversos SO's e ainda deixa os projetos perfomáticos.
    Em outras palavras, é uma ferramenta que permite <u>construir, versionar e executar containers</u> de forma padronizada. Ele utiliza <u>imagens docker</u>, que funcionam como moldes. Dessas imagens são criados containers, que são instâncias em execução. Cada imagem pode ser baseada em imagens oficiais mantidas por empresas ou comunidades.  
    Por fim, o Dockerfile é um arquivo de texto que contém instruções declarativas para a construção de uma imagem Docker. Nele são definidos a imagem base, as dependências necessárias, configurações e comandos que devem ser executados durante o processo de build.

- **Por que Docker?**  
    O Docker proporciona mais velocidade na configuração do ambiente de um dev, tem pouco tempo gasto em manutenção (containers são executados como configurados), a performance para executar aplicação, mais performático que uma VM e nos livra da Matrix From Hell.

### Seção 2: Trabalhando com Containers
- **O que é um Container?**  
    Containers não são máquinas virtuais completas, apesar de se comportarem de forma semelhante. Diferentemente das VMs, containers não possuem um SO próprio nem um kernel independente. Eles compartilham o kernel do SO do host, isolando apenas processos, sistema de arquivos, rede e permissões.  
    Na prática, o container cria um ambiente isolado que "simula" uma máquina virtual, não chegando a simular um computador inteiro, mas "parece" um sistema independente, que roda diretamente sobre o kernel do host. Isso permite que os containers sejam <u>muito mais leves e rápidos</u> do que máquinas virtuais tradicionais.
    Geralmente, eles utilizam <u>imagens enxutas</u> que contém apenas o necessário para executar uma aplicação específica. Por exemplo, uma imagem pode conter somente um servidor Redis ou um banco de dados ArangoDB, sem componentes extras de um SO completo. Embora seja possível usar imagens mais pesadas, a prática recomendada é manter as imagens pequenas e especializadas.

- **Containers são mais seguros?**  
    Normalmente expõem apenas as portas e recursos explicitamente configurados, o que ajuda no isolamento. No entanto, isso não garante segurança automaticamente, pois, uma configuração incorreta de portas, volumes ou permissões pode expor o container indevidamente.  

- **Containers e Docker juntos?**  
    Ao desenvolver uma aplicação que se comunica com containers, o desenvolvedor interage por meio das interfaces de rede configuradas, sem acessar diretamente o sistema do host.
    Quando chega o momento de colocar a aplicação em produção, as imagens Docker podem ser reutilizadas em diferentes ambientes, como servidores na AWS, Google Cloud ou em máquinas locais. Desde que o ambiente de destino possua um kernel Linux compatível, o comportamento do container será o mesmo, independentemente da distribuição Linux utilizada.
    Em sistemas como Windows e macOS, o Docker utiliza uma máquina virtual interna para fornecer um kernel Linux, permitindo que containers Linux sejam executados nesses sistemas. Nesse caso, não ocorre tradução entre sistemas operacionais, mas sim a execução sobre um kernel Linux virtualizado.


### Seção 3: Criando imagens e Avançando em containers
- **O que é uma Imagem?**  
    Imagens são originadas de arquivos que programamos para que o Docker crie uma estrutura que executa determinadas ações em containers. Elas contém informações como: imagens base, diretório base, comandos a serem executados, porta da aplicação e etc.  
    Ao rodar um container baseado na imagem, as instruções serão executadas em camadas.

- **Container VS Imagem**  
    Imagem é o "projeto" que será executado pelo container, todas as instruções estarão declaradas nela, já o Container é o Docker rodando alguma imagem, consequentemente executando algum código que foi proposto por ela.  
    O fluxo seria: programar uma imagem -> executar por meio de um container

- **Como criar e manipular uma Imagem?**  
    Para criar uma imagem, precisamos de um arquivo `dockerfile` em uma pasta que ficará o projeto. Este arquivo vai precisar de instruções para poder ser executado:
    - `FROM`: imagem base;
    - `WORKDIR`: diretório da aplicação;
    - `COPY`: quais arquivos precisam ser copiados;
    - `RUN`: roda um comando;
    - `EXPOSE`: porta da aplicação;
    - `CMD`: inicializa a aplicação.

    Para executar uma imagem primeiramente vamos precisar fazer o build, utilizando o comando `docker build <diretório da imagem>`. Depois utilizaremos o `docker run <imagem>` para executá-la.

    Para alterar uma imagem sempre vamos precisar fazer o build novamente. Para o Docker é como se fosse uma imagem completamente nova. Após fazer o build, vamos executá-la por outro id incremental único criada com o `docker run`.

    Além disso, podemos inicializar vários containers com a mesma imagem. As aplicações funcionarão em paralelo e para testar isso, podemos determinar uma porta diferente para cada uma e rodar no modo "detached".

- **Cache de Camadas (layers) das Imagens**  
    As imagens do docker são divididas em camadas (layers), onde cada instrução no Dockerfile representa uma layer. Quando algo é atualizado apenas as layers depois da linha atualizada são refeitas e o resto permanece em cache, tornando o build de imagem mais rápido.

- **Como utilizar os comandos Docker no terminal?**  
    Para rodar uma imagem, utilizamos a sintaxe: `docker run <imagem>`, na qual podemos encontrá-las através do site <a href="https://hub.docker.com"> hub.docker.com</a>.

    
    <details><summary>Principais Comandos do Terminal:</summary>

    |Comando|Definição|Exemplo|
    |:-:|:-:|:-:|
    |`docker ps`|Mostra os processos em execução| `docker ps`|
    |`docker container ls`| Assim como `ps`, exibe quais containers estão sendo executados no momento| `docker ls`
    |flag `-it`| Impede a parada automática da execução, rodando o container no modo iterativo, possibilitando executar comandos disponíveis no container.| `docker run -it ubuntu`|
    |`docker create --name meu_container imagem`| Usado para criar container sem iniciar|
    |flag `-a`| Obtem-se todos os containers já executados na máquina| `docker ps -a` |
    |flag `-d`| Utilizado para executar o container em background, para não precisar ficar com diversas abas de terminal aberto, chamado de modo "detached"| `docker run -d nginx`|
    |`docker stop`| força a parada da imagem | `docker stop <id ou name do container>`|
    |`docker start <id>`| Para voltar a rodar um container, já que o `run` sempre cria um novo container.| `docker start <id>`|
    | flag `--name`| Usado para definir o nome do container. Se não colocarmos, recebemos um nome aleatório.| `docker run -d -p 80:80 --name nginx_app nginx`|
    |`docker logs`| Usado para verificar o que ocorreu em um container, as últimas ações realizadas no container serão exibidas no terminal| `docker logs <id ou name>`|
    |flag `-f` | Usado para "seguir" o container. Chamado de follow. Sempre ao ocorrer algum acesso, alteração ou atualização será apresentado no terminal | `docker logs -f nginx_app`|
    |`docker -rm <id ou name>` |Remove um container da máquina que estamos executando o Docker. Se ainda . Dessa forma o container não é mais listado em `docker ps -a`.| `docker -rm nginx_app`|
    |`docker pull <imagem>`| Serve para baixar uma imagem Docker de um registro para o seu computador local, preparando-a para ser executada como um contêiner, e funciona baixando imagens por camadas, permitindo ter a versão mais recente disponível antes de criar um novo contêiner. A imagem fica em cache. | `docker run python`|
    | flag `--help`| Todo comando tem acesso à flag --help, dessa maneira, podemos ver todas as opções disponíveis nos comandos e também para relembrar algo ou executar uma tarefa diferente com o mesmo| `docker run --help`|
    |`docker tag <id> <nome>`| Serve para nomearmos a imagem que criamos. Também podemos modificar a tag, que seria como uma versão da imagem, semelhante ao git no versionamento. Para inserir a tag utilizamos `docker tag <id> <nome>:<tag>`|`docker tag ab1387asbe31 minhaimagem:minhatag`|
    |flag `-t`| Nomeia a imagem já na sua criação, sendo possível inserir o nome e a tag, na sintáxe nome:tag. Isso torna o processo de nomeação mais simples. | `docker build -t meunone_diferente .`|
    |`docker rmi <imagem>:<tag>` ou `docker image rm <IMAGEM>`| Remove imagens. Imagens que estão sendo utilizadas por um container, apresentarão um erro no terminal| `docker rmi meunode:minhatag`|
    |`docker system prune`| Remove todas as imagens, containers e networks não utilizados. Necessário confirmar para realizar a remoção.| `docker system prune`|
    |flag `--rm`|Remove container após utilizá-lo. Assim o container pode ser automaticamente deletado após sua utilização. Economizando espaço no computador e deixando ambiente mais organizado| `docker run --rm <container>`|
    |`docker cp`|Copia arquivos entre containers. Pode ser utilizado para copiar um arquivo de um diretório para um container ou de um container para um diretório determinado| `docker cp node_diferente2:/app/app.js ./copia/`|
    |`docker top <container>`| Usado para verificar dados de execução de um container. Temos acesso a quando ele foi iniciado, id do processo e descrição do comando CMD.| `docker top node_diferente2`|
    |`docker inspect <container>`| Usado para verificar diversas informações como ID, Data de criação, Imagem e entre outras. Serve para entender como o container está configurado. |`docker inspect node_diferente2`|
    |`docker stats`| Usado para verificar os processos que estão sendo executados em um container. Temos acesso ao andamento do processamento e memória gasta pelo mesmo.|`docker stats`|
    |`docker login`| Para autenticar-se pelo terminal, então inserindo usuário e senha. Assim, podemos enviar nossas próprias imagens para o HUB|`docker login`
    |`docker logout`| Remover a conexão entre nossa máquina e o Docker Hub.| `docker logout`
    |`docker push <imagem>`| Para enviar uma imagem criada ao Docker Hub. Porém antes é necessário criar o repositório para a mesma no site do Hub e estar também autenticado.| `docker push <username>/<imagem>`|
    |`docker pull <imagem>`| Para baixar a imagem do Docker Hub, podemos utilizar o comando pull e depois criar um novo container com `docker run <imagem>`.| `docker pull <username>/<imagem>`
    </details><br>

    Para **expor portas** devemos entender que os containers de docker não tem conexão com nada de fora deles, por isso precisamos expor portas, utilizando a flag `-p` (por exemplo: `docker run -d -p 80:80 nginx`). Dessa maneira, o container estará acessível na porta 80. Para compreender melhor, a porta (número) colocada antes dos dois pontos, é a porta que está expondo ao dispositivo que está atualmente usando. Depois dos dois pontos, é a porta que você deseja receber do container.
    Para atualizarmos uma imagem nossa que esteja no Docker Hub, devemos primeiramente fazer o `build`, trocando a tag da imagem para a versão atualizada. Depois fazemos um `push` novamente para o repositório.

### Seção 4: Introduzindo volumes aos nossos containers

- **O que são volumes?**  
    Uma forma prática de persistir dados em aplicações e não depender dos containers para isso. Todo dado criado por um container é salvo nele, então quando o container é removido perdemos os dados. Por isso, precisamos dos volumes para gerenciar os dados e também conseguir fazer backups de forma mais simples.

- **Tipos de volumes**  
    Os volumes são divididos em 3 tipos:
    - `Anônimos (anonymous)`: diretórios criados pela flag `-v`, porém com um nome aleatório. Não recomendado se queremos reutilizar durante a aplicação;
    - `Nomeados (named)`: são volumes com nomes, podemos nos referir a estes facilmente e saber para que são utilizados no nosso ambiente;
    - `Bind mounts`: uma forma de salvar dados na nossa máquina, sem o gerenciamento do Docker, informamos um diretório para este fim.

- **Comandos**
    <details><summary>Clique aqui</summary>

    |Comando|Definição|Exemplo|
    |:-----:|:-------:|:-----:|
    |`docker run -v /data`| Cria um volume anônimo, onde /data será o diretório que contém o volume anônimo. Este container estará atrelado ao volume anônimo. O próprio Docker fica encarregado de colocar em alguma pasta em /data|`docker run -d -p 80:80 --name phpmessages --rm -v /data phpmessages`|
    |`docker run -v nomedovolume:/data`| Cria um volume nomeado. Podendo ser facilmente referenciado. O diretório deve ser exatamente o mesmo colocado no WORKDIR do dockerfile.|`docker run -v phpvolume:/var/www/html/messages --rm phpmessages`|
    |`docker run /dir/data:/data`| Usado para criar um Bind Mount, que também é um volume, porém ele fica em um diretório que nós especificamos. Desta maneira, o diretório /dir/data no nosso computador, será o volume desse container. No entanto, não serve apenas para volumes, pois podemos utilizar para atualização em tempo real do projeto, sem ter que refazer o build a cada atualização do mesmo.|`docker run -d -p 80:80 --name phpmessage C:\20_DOCKER\arquivos\2_volumes\messages`|
    |`docker volume ls`| Usado para ver todos os volumes do nosso ambiente|`docker volume ls`|
    |`docker volume create <nome>`| Cria volumes manualmente também. Desta maneira temos um named volume criado, podemos atrelar a algum container na execução do mesmo.|`docker volume create volumeteste`|
    |`docker volume rm <nome>`| Remove um volume existente. Os dados serão removidos também.|`docker volume rm volumeteste`|
    |`docker volume prune`| Remove todos os volumes que não estão sendo utilizados.|`docker volume prune`|
    |`docker run -v volume:/data:ro`| Chamado de Volume apenas de Leitura (:ro = read only). Não tão utilizado, mas é útil em algumas aplicações.|`docker run -d -p 80:80 --name phpmessages_container -v volumeleitura:/var/www/html:ro --rm phpmessages`
    </details>

### Seção 5: Conectando containers com Networks
- **O que são networks?**  
    São uma forma de gerenciar a conexão do Docker com outras plataformas ou até mesmo entre containers. As redes (ou networks) são criadas separadas do containers, como os volumes. Além disso, existem alguns drivers de rede.  
    Uma rede deixa muito simples a comunicação entre containers.

- **Tipos de Conexão**
    Os containers costumam ter 3 principais tipos de conexão:
    - `Externo`: conexão com uma API de um servidor remoto;
    - `Com o Host`: comunicação com a máquina que está executando o Docker;
    - `Entre containers`: comunicação que utiliza o driver bridge e permite a comunicação entre dois ou mais containers.

- **Tipos de rede (drivers)**
    - `Bridge`: o mais comum e default do docker, utilizado quando containers precisam se conectar (na maioria das vezes optamos por este);
    - `Host`: permite a conexão entre um container à máquina que está hosteando o Docker;
    - `Macvlan`: permite a conexão à um container por um MAC address;
    - `None`: remove todas as conexões de rede de um container, ou seja, o container não pode conectar à nada.;
    - `Plugins`: permite extensões de terceiros para criar outras redes;

- **Comandos**
    <details><summary>Clique aqui</summary>

    |Comando|Definição|Exemplo|
    |:-----:|:-------:|:-----:|
    |`docker network ls`| Verifica todas as redes do nosso ambiente. Algumas redes já estão criadas, estas fazem parte da configuração inicial do Docker| `docker network ls`|
    |`docker network create <nome>`| Utilizado para criar uma rede. Sendo possível criar várias redes. Por default vem como o tipo bridge.|`docker network create minharedeteste`|
    |flag `-d`| Usado para definir um tipo específico de driver para a rede|`docker network create -d macvlan meumacvlan`|
    |`docker network rm <nome>`| Usado para remover uma rede. Deve-se tomar cuidado com containers já conectados.|`docker networm rm minharedeteste`|
    |`docker network prune`| Remove redes que não estão em execução/utilizadas| `docker network prune`|
    |flag `--network`| Utilizado para relacionar o container à uma rede| `docker run -d -p 3306:3306 --name mysql_api_container --rm --network flasknetwork -e MYSQL_ALLOW_EMPTY_PASSWORD=True mysqlapinetwork`|
    |`docker network connect <rede> <container>`| Conecta manualmente um container já existente a uma rede|`docker network connect flasknetwork 947ac7c40e03`|
    |`docker network disconnect <rede> <container>`| Desconecta manualmente um container da rede.| `docker network disconnect flasknetwork 947ac7c40e03`|
    |`docker network inspect <rede>`| Usado para analisar os detalhes de uma rede, recebendo informações como Data de criação, driver, nome e outros.|`docker network inspect flasknetwork`|
    </details>

### Seção 6: Introdução ao YAML
- **O que é YAML?**  
    É uma linguagem de serialização/configuração. Seu nome é YAML ain't Markup Language (YAML não é uma linguagem de marcação)
    Usada geralmente para arquivos de configuração, inclusive do Docker, para configurar o Docker Compose, sendo de fácil leitura para nós humanos.
    A extensão dos arquivos é `.yml` ou `.yaml`.

- **Arquivo YAML e suas diretrizes:**  
    - O arquivo `.yaml` geralmente possui chaves e valores, que é de onde vamos retirar as configurações do nosso sistema.  
    - Para definir uma chave apenas inserimos o nome dela e em seguida colocamos dois pontos e depois o valor.
    - O fim de uma linha indica o fim de uma instrução, não há ponto e vírgula;
    - A identação deve conter um ou dois espaços e não devemos utilizar TAB. E cada uma define um novo bloco;
    - O espaço é obrigatório após a declaração da chave.

- **Instalação do Pacote YAML:**  
    Para instalar o pacote YAML no python deve-se utilizar o comando `pip3 install pyyaml`
- **Estruturas e tipos da Linguagem YAML**:  
    <details><summary>Clique aqui</summary>

    |Elementos YAML|Código|Definição|Exemplo|
    |:---------------:|:----:|:-------:|:-----:|
    | Comentário | `#` | Possível comentar no YAML também. O processador de YAML ignorará comentários.| `# Instruções para o programa`|
    | Dados numéricos | | Temos dois tipos, sendo eles Decimal e Inteiro| `pi = 3.14`<br>`inteiro = 242`|
    | String | `""` e sem aspas| Para formar strings podemos usar aspas duplas ou sem aspas e mesmo assim será interpretado como string. |`Sem aspas: este é um texto válido`<br>`Com aspas: "e este também"`|
    | Valores Nulos | `~` ou `null` | Define um dado como nulo, nas duas formas. Os dois vão resultar em None, após a interpretação. | `nulo: ~`<br>`nulo_dois: null` |
    | Booleanos | `True`/`On`<br>`False`/`Off` | Define dados como booleanos, utilizando True ou On e False ou Off. | `verdadeiro: True`<br>`verdadeiro_2: On` <br>`falso: False`<br>`falso_2: Off`|
    | Listas | `[]` ou  `chave:`<br>`- item1`<br>`- item2` | Tipos de dados para listas/arrays, possui essas duas sintaxes. As listas não tem essa premissa de que devem em cada uma ter somente um tipo de dado único. | `lista: [1,2,3,4,5]`<br>|
    | Dicionários | `{}` ou `objeto:`<br>`chave: 1`<br>`chave: 2`| Tipo de dados para simular objetos ou listas com chaves-valores. Tendo duas formas de sintaxe. Podemos colocar um objeto dentro de um objeto também. | `obj: {a: 1, b: 2, c: 3}` |
    </details>

### Seção 7: Gerenciando Múltiplos Containers com Docker Compose
- **O que é Docker Compose?**  
    Docker Compose é uma ferramenta para rodar múltiplos containers, essencial para quando o projeto começa a escalar. Teremos apenas um arquivo de configuração, que orquestra totalmente esta situação.  
    É uma forma de <u>rodar múltiplos builds e runs</u> com um comando.  
    Em projetos maiores é essencial o uso do Compose.
    O Compose cria uma rede básica Bridge entre os containers da aplicação, porém podemos isolar as redes com a chave `networks:`. Dessa maneira, podemos conectar apenas os containers que optarmos e podemos definir drivers diferentes também.  
    O Compose possibilita também gerar o build, eliminando o processo de gerar o build da imagem a cada atualização. Utilizamos a chave `build:`

- **Como utilizar o Compose?**  
    Primeiramente deve-se criar um arquivo chamado `docker-compose.yml` na raiz do projeto. Este arquivo vai coordenar os containers e imagens, e possui algumas chaves muito utilizadas:
    - `Version`: versão do compose;
    - `Services`: containers/serviços que vão rodar nessa aplicação;
    - `Volumes`: possível adição de volumes.
    <details><summary>Exemplo de Compose</summary>

    ```YAML
    version: '3.3'
    services:
        db: # Container de MySQL
            image: mysql:5.7 # FROM mysql:5.7
            volumes:
                - db_data:/var/lib/mysql
            restart: always
            environment:
                MYSQL_ROOT_PASSWORD: wordpress
                MYSQL_DATABASE: wordpress
                MYSQL_USER: jocimar
                MYSQL_PASSWORD: secret
        wordpress:
            depends_on:
                - db
            image: wordpress:latest
            ports:
                - "8000:80"
            restart: always
            environment:
                WORDPRESS_DB_HOST: db:3306
                WORDPRESS_DB_USER: jocimar
                WORDPRESS_DB_PASSWORD: secret
                WORDPRESS_DB_NAME: wordpress
    volumes:
        db_data: {}
    
    ```
    </details><br>

- **Comandos**
    <details><summary>Clique aqui</summary>

    |Comando| Definição |
    |:-----:|:---------:|
    |`docker-compose up`| Roda a estrutura Compose. Isso fará com que as instruções no arquivo sejam executadas, da mesma forma que realizamos os builds e também os runs. Pode-se parar o Compose com `CTRL+C` no terminal|
    |`docker-compose down`| Usado para parar o Compose que roda em background. Dessa maneira o serviço para e os containers que estavam relacionados são adicionados ao `docker ps -a`|
    |`docker-compose ps`| Recebe um resumo dos serviços que sobem ao rodar o compose. |
    </details>

    Para definirmos as variáveis de ambiente para o Docker Compose, é necessário criar um arquivo base `env_file (.env)`. As variáveis podem ser chamadas pela sintaxe: `${VARIAVEL}`. Essa técnica é útil quando o dado a ser inserido é sensível/não pode ser compartilhado, como uma senha.


### Seção 8: Docker Swarm para orquestração
- **O que é orquestração de containers?**
    Orquestração é o ato de conseguir gerenciar e escalar os containers da nossa aplicação. Temos um serviço que rege sobre outros serviços, verificando se os mesmos estão funcionando como deveriam. Desta forma, conseguimos garantir uma aplicação saudável e também que esteja sempre disponível.  
    **Alguns serviços: Docker Swarm, Kubernetes e Apache Mesos.**
    A Orquestração de containers é um problema que pode ser resolvido com um destes citados acima. Para conseguir gerir projetos maiores temos que escalar a aplicação em várias máquinas para que os usuários não sintam lentidão, erros por falta de memória no servidor, de processamento e etc... Então é neste momento que entra este Cluster, onde ao invés de utilizar uma arquitetura vertical (com um máquina grande suportando tudo), usamos uma Arquitetura Horizontal, na qual diversas máquinas menores são usadas para que possa servir a aplicação em cada uma delas. Geralmente se opta pela horizontal por questões de custos financeiros.

- **O que é Docker Swarm?**
    Uma ferramenta do Docker para orquestrar containers, podendo escalar horizontalmente nossos projetos de maneira simples, mais conhecido como "cluster".  
    A facilidade do Swarm para outros orquestradores é que todos os comandos são muito semelhantes ao do Docker.  
    (Necessário habilitar o Swarm após a instalação do Docker).

- **Como utilizar o Swarm?**
    Temos alguns conceitos fundamentais que são utilizados:
    - `Manager Node`: node que gerencia os demais nodes;
    - `Worker Node`: nodes que trabalham em função do Manager;
    - `Service`: conjunto de tasks que o Manager Node manda o Work Node executar;
    - `Task`: comandos que são executados nos Nodes;
    - `Nodes`: é uma instância (máquina) que participa do Swarm;

    Para executar o Swarm temos dois jeitos: AWS (pago) ou Docker Labs (gratuito, porém expira a cada 4 horas).

- **Comandos**
    <details><summary>Clique aqui</summary>

    |Comando|Definição|Exemplo|
    |:-----:|:-------:|:-----:|
    |`docker swarm init`|Inicia o Swarm. Em alguns casos é necessário declarar o IP do servidor com a flag: `--advertise-addr`. O comando fará com que a instância vire um Node, transformando também o Node em um Manager|`docker swarm init --advertise-addr 192.168.0.23`|
    |`docker node ls`|Exibe no terminal quais Nodes estão ativos. Podemos assim monitorar o que o Swarm está orquestrando|
    |`docker swarm join --token <TOKEN> <IP>:<PORTA>`| Comando usado para adicionar novos Nodes, conectando desta forma a máquina à outra. Esta nova máquina entra na hierarquia como Worker. Todas as ações (tasks) utilizadas no Manager, serão replicadas em Nodes que foram adicionados com join. |
    |`docker swarm leave`| Para de executar o Swarm em uma determinada instância, mudando seu status para Down. A partir desse momento, a instância não é mais contada como um node para o Swarm.|
    |`docker node rm <ID>`| Remove um Node do nosso ecossistema do Swarm. Dessa forma, a instância não será mais considerada um Node, saindo do Swarm. O container mantém rodando na instância.|
    |`docker service create --name <nome> <imagem>`| Inicia um novo serviço com o comando. Dessa forma um container novo é adicionado ao nosso Manager. Este serviço estará sendo gerenciado pelo swarm.| `docker service create --name nginxswarm -p 80:80 nginx`|
    |`docker service ls` | Lista todos os serviços que estão rodando |
    |`docker service rm <nome>`| Remove um serviço, fazendo-o por consequência parar de rodar e parar um container que está rodando.
    |`docker service create --name <NOME> --replicas <NUMERO> <IMAGEM>`| Cria um serviço com um número maior de réplicas, dessa maneira uma task será emitida, replicando este serviço nos Workers. |
    |`docker swarm join-token manager`| Usado para checar o token do Swarm, para dar join em alguma outra instância futuramente.|
    |`docker service inspect <ID>`|Inspeciona os detalhes de um serviço|
    |`docker service ps <ID>`| Mostra quais containers um serviço já rodou. Recebe uma lista de containers que estão rodando e também os que já receberam baixa. Semelhante ao docker ps -a.|
    |`docker stack deploy -c <ARQUIVO.YAML> <NOME>`| Para rodar Compose com Swarm. Teremos então o arquivo compose sendo executado|
    |`docker service scale <NOME>=<REPLICAS>`| Cria novas réplicas nos Worker Nodes, dessa forma as outras máquinas receberão as tasks a serem executadas.|`docker service scale nginx_swarm_web=3`|
    |`docker node update --availability drain <ID>`| Faz com que um node não receba mais "ordens" do Manager. O status de Drain é o que não recebe tasks. Podemos voltar para "active", então o serviço volta ao normal.|
    |`docker service update --image <IMAGEM> <SERVICO>`| Atualiza as configurações/parâmetros dos Nodes, no caso a imagem. Dessa forma, apenas os nodes com status ACTIVE irão receber as atualizações.|
    |flag `--network`|docker network create| A conexão entre instâncias usa um driver diferente, o overlay. Primeiramente devemos criar a rede com `docker network create` e depois criar um service com a flag --network, para inserir as instâncias na nossa nova rede.|
    |`docker service update --network-add <REDE> <NOME>`| Conecta um serviço que já está em execução à uma rede
    </details>

### Seção 10: Orquestração com Kubernetes
- **O que é Kubernetes?**  
    É uma ferramenta criada pelo Google de orquestração de containers, onde permite a criação de múltiplos containers em diferentes máquinas (nodes), escalando projetos e formando um cluster. Kubernetes gerencia serviços, garantindo que as aplicações sejam executadas sempre da mesma forma.

- **Conceitos fundamentais**  
    - `Control Plane`: onde é gerenciado o controle dos processos dos nodes;
    - `Nodes`: máquinas que são gerenciadas pelo Control Plane;
    - `Deployment`: A execução de uma imagem/projeto em um Pod;
    - `Pod`: um ou mais containers que estão em um Node;
    - `Services`: serviços que expõe os Pods ao mundo externo;
    - `Kubectl`: cliente de linha de comando para o kubernetes.

- **Como utilizar o Kubernetes?**  
    Kubernetes pode ser executado de uma maneira simples, porém tem duas dependências: O client (kubectl) que é a maneira de executar o Kubernetes e o Minikube, uma espécie de simulador de Kubernetes para não precisar de vários computadores/servidores.

    <details><summary>Comandos do Terminal</summary>

    |Comando|Definição|Exemplo|
    |:-----:|:-------:|:-----:|
    |`minikube start --driver=<DRIVER>`| Inicializa o Minikube. Para testar, utilizamos `minikube status`. Sempre que fomos utilizar é necessário inicializar, então precisamos dar esse comando.|`minikube start --driver=docker`|
    |`minikube stop`| Para a execução do minikube|
    |`minikube dashboard` ou `minikube dashboard --url`| Acesso ao dashboard para ver todo o detalhamento do projeto (serviços, pods e etc)|
    |`kubectl create deployment <NOME> --image=<IMAGEM>`| Após fazer upload da imagem no Docker Hub, utilizamos esse comando que cria um deployment|
    |`kubectl get pods`| Usado para verificar os pods|
    |`kubectl describe pods`| Usado para saber mais detalhes|
    |`kubectl config view`| Usado para verificar como o Kubernetes está configurado, recebendo informações importantes baseadas no Minikube, que é onde o Kubernetes está sendo executado.|
    |`kubectl expose deployment <NOME> --type=<TIPO> --port=<PORT>`| Cria um serviço e expõe os Pods. Colocamos o nome do deployment já criado. O tipo de Service, há vários para se utilizar, porém o LoadBalancer é o mais comum, onde todos os Pods são expostos. E uma porta para o serviço ser consumido|`kubectl expose deployment flask-deployment --type=LoadBalancer --port=5000`|
    |`minikube service <NOME>`| Usado para gerar o IP e acessar o serviço, dessa forma o IP aparece no terminal e também uma aba no navegador é aberta com o projeto.|`minikube service flask-deployment`|
    |`kubeclt get services`| Usado para obter detalhes dos Services disponíveis e já criados.|
    |`kubeclt describe services/<NOME>`| Usado para obter informações de um serviço em específico.|
    |`kubectl scale deployment/<NOME> --replicas=<NUMERO>`| Usado para replicar a aplicação. Utilizado tanto para aumentar o número de réplicas como diminuir. | `kubectl scale deployment/flask-deployment --replicas=3`|
    |`kubectl get rs`| Usado para checar o número de réplicas|
    |`kubectl set image deployment/<NOME> <NOME_CONTAINER>=<NOVA_IMAGEM>`| Usado para atualizar a imagem.|
    |`kubectl rollout status deployment/<NOME>`| Usado para verificar se houve uma alteração.|
    |`kubectl rollout undo deployment/<NOME>`| Desfaz a alteração feita.|
    |`kubectl delete service <NOME>`| Usado para deletar um Service, fazendo com que os Pods não tneham mais a conexão externa, ou seja, não é possível mais acessá-los|
    |`kubectl delete deployment<NOME>`| Usado para deletar um deployment, dessa maneira, o container não estará mais rodando, pois parará os Pods. Assim, precisaria criar um deployment novamente com a mesma ou outra imagem, para acessar algum projeto.|
    |`kubectl apply -f <ARQUIVO>`| Usado para executar o arquivo de Deployment ou o arquivo de Service (arquivo .yaml)|
    |`kubectl delete -f <ARQUIVO>`| Usado para parar a execução do deployment/service baseado em arquivo (o declarativo)|
    </details><br>

- **Modo Declarativo no Kubernetes**  
    O modo declarativo é guiado por um arquivo, semelhante ao Docker Compose. Utilizamos ele pois tornamos nossas configurações mais simples e centralizadas tudo em um comando. Esse arquivo também é escrito em linguagem YAML.
    Assim como no Compose, ele tem as chaves mais utilizadas:
    - `apiVersion`: versão utilizada da ferramenta;
    - `kind`: tipo do arquivo (Deployment, Service);
    - `metadata`: descrever algum objeto, inserindo chaves como name;
    - `replicas`: número de réplicas de Nodes/Pods;
    - `containers`: definir as especificações de containers, como nome e imagem.

### REGEX com Python
- **O que é uma Expressão Regular?**  
    Basicamente, servem para dedefinir um determinado padrão de string e buscar/verificar se determinada string pertece/contém àquele padrão, ou seja, uma forma na qual definimos um padrão e buscamos se sua existência há em outras strings.

- **Como utilizar o REGEX?**  
    Primeiramente devemos importar a biblioteca `import re`.
    Para criarmos um padrão, usamos o comando `re.compile(padrão)`

    |Comando|Definição|Exemplo|
    |:-----:|:-------:|:-----:|
    |`re.fullmatch()`| Basicamente, compara se uma string é inteiramente correspondente ao padrão estabelecido. Se a String não atender ao padrão, retornará `none`, senão, retornará um objeto do tipo `re`.| `re.fullmatch(padrao, string)`|
    |`re.search()`| Percorre toda a string e verifica se há partes da string(caracteres) que correspondem ao padrão, satisfazendo-o. No entanto, se houver duas ou mais partes, o searh só pegará a primeira|`re.search(padrao, string)`|
    |`re.findall`| Percorre toda a string e verifica se há partes que satisfaçam o padrão, porém, se houver duas ou mais partes nessa condição, ele irá capturar todos.

    |Sintaxe|Símbolo|Definição|
    |:-----:|:-----:|:-------:|
    |`.`| ponto | Representa qualquer caractere, menos `\n`|
    |`[]`| colchetes | Serve para definir um conjunto de operações na qual podem acontecer dentro. Representa um conjunto de possibilidades|
    |`^`| circunflexo| Representa o início da string|
    |`$`| cifrão| Representa o final da string|
    |`[^]`| colchetes+circunflexo| Representa "diferente de" um caractere|
    |`\w`| barra + w| Representa a verificação "is alfanum"|
    |`\W`| barra + W| Representa a verificação "not is alfanum"|
    |`\s`| barra + s| Representa caracter vazio|
    |`\S`| barra + S| Representa "não vazio"|
    |`\d`| barra + d| Representa números de 0 à 9|
    |`\D`| barra + D| Representa "not in 0-9", ou seja, numeros que não sejam de 0 à 9|
    |`-`| hífen| Representa um intervalo à outro. Exemplo: `a-zA-Z0-9`|
    |`+`| mais| Representa algo que aparecerá uma ou mais vezes. Usado também para retornar todos os caracteres, no caso de uma função ``fullmatch()`|
    |`*`| asterisco| Representa 0 ou mais vezes|
    |`?`| interrogação| Representa 0 ou 1|
    |`{x}`| chaves+x| Representa "x vezes"|
    |`{z,y}`| chaves+z+y| Representa "z mínimo y máximo" vezes|

# 👁‍🗨 Evidências
Como não houveram exercícios nesta Sprint, consequentemente não há evidências deles.

# ✍ Exercícios
Não houveram exercícios nesta Sprint.

# 🎯 Desafio da Sprint
O desenvolvimento do desafio da sprint e seus respectivos arquivos relacionados encontram-se em sua pasta, assim como seu README que fora usado para dissertar sobre os passos executados e resultados.
O Readme do Desafio foi dividido em etapas, seguindo a lógica proposta pela Compass e tais quais apresentam e explicam as resoluções utilizadas e os resultados obtidos:
- 📁[Pasta do Desafio](../Sprint%205/Desafio/)
- 📝[README do Desafio](../Sprint%205/Desafio/README.md)
    
# ✅ Certificados
Não houveram cursos externos, apenas dentro da Compass Udemy.