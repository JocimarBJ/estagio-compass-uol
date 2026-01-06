# 📝 Resumo
 
|<h3>🔍ÍNDICE</h3>|
|------------------|
| [🧠 Competências Aplicadas](#-competências-aplicadas) |
| [🐍 Curso: Python 3 - Do básico ao avançado](#-curso-python-3---do-básico-ao-avançado) |
| [🟢 Seção 2: Introdução Python](#-seção-2-introdução-python) |
| [🔧 Seção 3: Configuração do Ambiente Python](#-seção-3-configuração-do-ambiente-python) |
| [▶️ Seção 4: Executando Código Python](#-seção-4-executando-código-python) |
| [📚 Seção 5: Fundamentos de Python](#-seção-5-fundamentos-de-python) |
| [🧩 Seção 7: Estruturas de Controle](#-seção-7-estruturas-de-controle) |
| [📂 Seção 9: Manipulação de Arquivos](#-seção-9-manipulação-de-arquivos) |
| [⚡ Seção 10: Comprehension](#-seção-10-comprehension) |
| [🔃 Seção 11: Funções](#-seção-11-funções) |
| [🧱 Seção 13: Programação Orientada à Objetos](#-seção-13-programação-orientada-à-objetos) |
| [🔁 Seção 15: Programação Funcional](#-seção-15-programação-funcional) |
| [🧪 Seção 17: Isolamento de Ambientes](#-seção-17-isolamento-de-ambientes) |

## 🧠 Competências aplicadas
- Lógica de programação  
- Sintaxe e fundamentos da linguagem Python  
- Tipos de dados, operadores e estruturas nativas  
- Estruturas de controle (condicionais, laços e exceções)  
- Manipulação de listas, tuplas, dicionários e conjuntos  
- Comprehensions e generators  
- Programação funcional (`lambda`, `map`, `filter`, `reduce`)  
- Funções de primeira classe e de alta ordem  
- Closures, recursão e imutabilidade  
- Lazy evaluation e uso de iteradores  
- Programação Orientada a Objetos (POO)  
- Boas práticas e legibilidade de código (Zen of Python)  
- Manipulação de arquivos (`with`, `csv`, streaming)  
- Uso de ambientes virtuais (`.venv`) 

## 🐍 Curso: Python 3 - Do básico ao avançado
### 🟢 Seção 2: Introdução Python
- **O que é Python?** <br>
    Python está em primeiro lugar entre as linguagens de programação no quesito popularidade, lançada em 1991 e mantida até hoje pela fundação Python Software Fundation, mantendo como código aberto.<br>
    Ela é a linguagem mais usada para aprendizagem, uma vez que é de alto nível e sua sintaxe é simples. <br>
    Python é uma ***linguagem Dinâmica*** e ao mesmo tempo ***fortemente tipada***.

- **Onde Python é muito usado?** <br>
    Desenvolvimento Web Backend, IAs, Big Data, Data Science e etc.

- **Zen Of Python** <br>
    O python tem suas próprias filosofias, propriamente dito como Estilo de Codificação ou PEP8, trazendo boas práticas e padronização para os desenvolvedores.

- <details><summary>Conceitos</summary>

    > *Por Tim Peters*

    - **Bonito é melhor que feio.**
    - **Explícito é melhor que implícito.**
    - **Simples é melhor que complexo.**
    - **Complexo é melhor que complicado.**
    - **Plano é melhor que aninhado.**
    - **Esparso é melhor que denso.**
    - **Legibilidade conta.**
    - **Casos especiais não são especiais o bastante para quebrar as regras.**
    - **Embora a praticidade vença a pureza.**
    - **Erros nunca devem passar silenciosamente.**
    - **A menos que sejam explicitamente silenciados.**
    - **Diante da ambiguidade, recuse a tentação de adivinhar.**
    - **Deveria haver uma — e preferencialmente apenas uma — maneira óbvia de fazer isso.**
    - **Embora essa maneira possa não ser óbvia à primeira vista, a menos que você seja holandês.**
    - **Agora é melhor que nunca.**
    - **Embora nunca seja frequentemente melhor do que *agora*.**
    - **Se a implementação é difícil de explicar, é uma má ideia.**
    - **Se a implementação é fácil de explicar, pode ser uma boa ideia.**
    - **Namespaces são uma grande ideia — vamos fazer mais delas!**
    </details>

### 🔧 Seção 3: Configuração do Ambiente Python
Durante as aulas do curso, fomos instruídos à instalar o Python 3 e o Anaconda, configurando o Jupyter Navigator para as futuras resoluções.

### ▶️ Seção 4: Executando Código Python
Podemos executar um código python utilizando o interpretador próprio da linguagem através de linhas de comando no terminal. Também através do Jupyter ou no VSCode.

### 📚 Seção 5: Fundamentos de Python
Nessa seção retratamos sobre a forma que funcionam as sentenças de Python.
- Python se importa com as indentações e quebras de linha
- Para acessar uma explicação sobre um comando, utilizamos `help(print)`. (Print foi um exemplo).

<details><summary style="font-weight:bold"> Tipos Básicos:</summary>

- Alguns dos principais tipos de valores da linguagem Python são: 
    |Tipo|Categoria|Exemplo| Definição|
    |:--:|:-------:|:-----:|:-|
    |bool| Booleano| `True` e `False`| Falso ou Verdadeiro, 0 ou 1
    |int | Inteiro | `1, 2, -10...`| Números sem vírgula
    |float | Ponto Flutuante| `1.2, -5.3...`| Números Reais
    |str|String| `'Maria Clara'`, `"João"`| Sequência de caracteres e letras que pode ser delimitado por aspas simples ou duplas
    |list| Lista Dinâmica| `[1,2,'abcde']`| Estrutura indexada na qual acessamos a partir de um índice
    |dict | Dicionário | `{'nome': 'Maria Clara', 'idade':21}`| estrutura chave-valor, na qual acessamos a partir da chave definida entre {}
    |NoneType| Nulo/Undefined | `None`| A ausência de valor

</details>

<details><summary style="font-weight:bold">Variáveis</summary>

Quando criamos uma variável em python, não definimos o tipo dessa variável, ou seja, dinamicamente o interpretador vai descobrir qual tipo de variável é.
No entanto, por ser uma linguagem fortemente tipada e dinâmica, significa que o Python sempre estará ciente sobre a existência dos tipos e faz a validação se podemos ou não fazer determinadas operações, no entanto não irá bloquear você de, a partir de uma única variável, colocar diferentes tipos nessa variável. Em suma, Python é dinamicamente tipada, mas fortemente tipada, ou seja, o tipo não é declarado explicitamente, porém o Python não permite operações inválidas entre tipos diferentes.
</details>

<details><summary style="font-weight:bold">Comentários e Boas Práticas</summary>

Existem os comentários de uma única linha e múltiplas linhas.

```Python
# Comentário de uma única linha

"""Comentários
de múltiplas linhas"""

'''Isso também 
funciona'''
```

Comumente utilizamos os comentários para contextualizar, sendo utilizado geralmente acima da linha de comando na qual você está retratando.
</details>

<details><summary style="font-weight:bold">Operadores</summary>

- #### Operadores Aritméticos
    Temos tais operadores aritméticos para python:
    | Tipo | Símbolo | Definição |
    |:----:|:-------:|:---------:|
    |Soma|+| Somatória|
    |Subtração|-| Subtração normal|
    |Multiplicação|*| Multiplicação normal|
    |Divisão|/| Divisão normal|
    |Divisão Inteira|//| Divide, mas apresenta como inteiro|
    |Exponenciação|**| Multiplica por ele mesmo|
    |Módulo|%| Retorna resto da divisão|

    Sendo eles podendo ser prefixados ou posfixados.

- #### Operadores Relacionais
    |Símbolo|Definição|
    |:-:|:-:|
    |`>` | maior que...
    |`>=` | maior ou igual que...
    |`<` | menor que...
    | `<=` | maior ou igual que...
    | `!=` | diferente de...
    | `==` | igual à...


- #### Operadores de Atribuição
    São operações que abreviam operações, pegando o operador de atribuição e os operadores relacionais
    |Símbolo|Definição|
    |:-:|:-:|
    | `=` | atribuição simples;
    | `+=` | soma o conteúdo da variavel + o conteudo e atribui à ela mesma,<br>ex: `a+=5` é o mesmo que `a=a+5`;
    | `-=` | subtração, segue a mesma lógica;
    | `*=` | multiplicação, segue a mesma lógica;
    | `/=` | divisão, segue a mesma lógica;
    | `//=` | divisão de inteiro, segue a mesma lógica;
    | `%=` | módulo, segue a mesma lógica;
    | `**=` | exponenciação, segue a mesma lógica.

    Em python não existe `a++`, nesse caso devemos usar `a+=1`

- #### Operadores Lógicos
    `True or False` - operam em cima de resultados, expressões ou valores, ex. `7 != 3 and 2 > 3`<br>
    Utilizamos a tabela verdade para isso:
    |Tabela AND |Resultado|
    |:-:|:-:|
    |True and True |True
    |True and False | False
    |False and True | False
    |False and False | False

    |Tabela OR|Resultado|
    |:-:|:-:|
    |True or True |True
    |True or False | True
    |False or True | True
    |False or False | False

    |Tabela XOR|Resultado|
    |:-:|:-:|
    |True != True | False
    |True != False | True
    |False != True | True
    |False != False | False

    |Tabela Negação(unário)|Resultado|
    |:-:|:-:|
    | not True | False
    | not False | True
    | not 0 | True (zero é falso)
    | not 1 | False (qualquer numero é verdadeiro)
    | not not 0 | False
    | not not True | True

    **Operadores Bit-Bit**<br>
    Operadores bit a bit operam bit a bit, não sobre valores booleanos diretamente. Embora lembrem operadores lógicos, não devem ser usados como substitutos de and / or.
    - `&` - AND
    - `|` - OR
    - `^` - XOR

- #### Operadores Ternários
    Os operadores ternários funcionam com três operandos, sua sintaxe é:
    ```Python
    resultado = valor_se_verdadeiro if condicao else valor_se_falso
    ```

- #### Operadores Membro/Identidade
    Serve para saber se determinado elemento faz parte ou é membro da lista.
    - Exemplo:

        ```Python
        #Operador de membro
        lista = [1,2,3,'Ana', 'Carla']
        2 in lista          #operação aqui
        'Ana' not in lista  #operação aqui

        #Operador de Identidade
        x=3, y=x, z=3
        x is y
        y is z
        x is not z
        ```


<!--Final Operadores-->
</details>

<details><summary style="font-weight:bold">Builtins</summary>

As funções como `type()`, `help()`, `print()` e etc, fazem parte do namespace built-in e podem ser usadas diretamente, sem importação.
Para usarmos precisamos fazer algo como:
```Python
__builtins__.type('Fala galera')
__builtins__.help(__builtins__.dir)
```

</details>

<details><summary style="font-weight:bold">Conversão de Tipos</summary>

Para fazermos a conversão de variáveis para outros tipos, podemos fazer da seguinte maneira:
```Python
a = 1
b = '2'

a = a + int(b)
#Também chamado de Casting
```


</details>

<details><summary style="font-weight:bold">Coerção Automática</summary>

O python em situações em que não há ambiguidade ele ativa a coerção automática propriamente da linguagem.
A coerção automática ela identifica automaticamente qual tipo aquela variável se refere, sem a necessidade de uma declaração explícita.
</details>

<details><summary style="font-weight:bold">Tipos Numéricos</summary>

Utilizando a função `dir()` podemos identificar diversas funções relacionadas ao tipo passado como parâmetro entre os parênteses, como `__abs__`, `__add__`, `is_integer` e entre outros. Estes podem ser utilizados colocando um ponto e digitando (`.__add__`, `.__abs__`) ou podem ser substituídos pela função em si, como `abs()`, `add()` e etc.
Como as linguagens geralmente usam métodos de operações aritméticas que são amplamente usados porque trazem uma série de vantagens como eficiência e velocidade, elas não utilizam uma especificação 100% precisa, que pode ser lenta. Dessa forma, erros podem ocorrer durante os cálculos, então recomenda-se utilizar, por exemplo no caso dos números decimais, a biblioteca `Decimal`, na qual o Python disponibiliza e que traz um nível de precisão excelente.
</details>

<details><summary style="font-weight:bold">Strings</summary>

Para utilizarmos Strings na linguagem Python temos que utilizar aspas duplas ou aspas simples.
Dentro de uma variável, cada letra da string pode ser acessada considerando como um vetor, onde cada letra esteja num índice.<br>
Exemplo:
```Python
nome = "Ana Paula"... 
nome[0] # pega da esquerda para a direita, resultado: 'A'
nome[-3] # pega da direita para a esquerda, resultado: 'u'
nome[4:] # pega tudo após o índice 4, resultado: 'Paula'
nome[:3] # pega tudo antes do índice 3, resultado: 'Ana'
nome[2:5] # pega tudo entre os índices 2 e 5, resultado: 'a P'

nome[::2] # pega todos pulando de 2 em 2, resultado: 'AaPua'
nome[1::2] # pega a partir do indice 1 e vai pulando de 2 em 2, resultado: 'n al'
nome[::-1] # inverte a string, resultado: 'aluaP anA'
```

Também foi mostrado algumas funções próprias para strings, como `lower()`, `upper()` e `split()`.
</details>

<details><summary style="font-weight:bold">Listas, Tuplas, Dicionários e Conjuntos</summary>

**Listas**: Em Python a lista é comparável ao Array do JavaScript, onde é uma sequência mutável e indexada, o que significa que podemos adicionar ou remover itens da lista. Outra característica é que a lista cresce dinamicamente e é heterogênea, ou seja, aceita diversos tipos dentro de si.<br>

- `append()`, onde usamos para adicionar um elemento;
- `remove()`, onde remove um elemento da lista;
- `reverse()`, onde diferente da string, ao invés de inverter somente visualmente para a saída, é invertido os elementos em si dentro da lista.

**Tuplas**: Já as Tuplas (ou `Tuple()`) diferentemente das listas, elas não podem ser modificadas.<br>
Exemplo de Tupla: `tupla = ('morango', 'limão', 'maçã')`

**Dicionários**: Normalmente ela é indexada com String, mas também pode ser indexada com outros tipos. Esse valor indexado é chamado de Chave e logo após definida a chave adicionamos o Valor que será relacionado à ela.<br>
Exemplo: `pessoa = {'nome': 'Ana', 'idade':43, 'cursos': ['React', 'Node', 'Angular']}`<br>
Tendo funções como `pop()`, `update()`, `get()`, `clear()` e etc, que auxiliam para alterações internas, remoção ou consultar. 

**Conjuntos**: Diferente das Listas, os conjuntos não garantem ordem de inserção, não é indexado e não aceita repetições. Neste temos funções como `set()`, `union()`, `intersection()`e `update()`, além de outras formas de interação entre os conjuntos, como:
```Python
c2 <= c1 # c2 é subconjunto de c1? 
# OU
c1 >= c2 # c1 é superconjunto de c2?
```

**Em Resumo temos**:
|Estrutura| Tipo | Ordenado | Mutável | Construtor | Exemplo|
|:-:|:-:|:-:|:-:|:-:|:-:|
|list | Lista | Sim | Sim | `[]` ou `list()` | `[1, 2.5, 'Pedro', True]`|
|tuple | Tupla | Sim | Não | `()` ou `tuple()` | `(1, 2.5, 'Pedro', True)`|
|set | Conjunto | Não | Sim | `{}` ou `set()` | `{1, 2.5, 'Pedro', True}`|
|dictionary | Dicionário | Sim | Sim | `{}` ou `dict()` | `{6: 'jun', 7:'jul'}`|
</details>

<details><summary style="font-weight:bold">Interpolação</summary>

Assim como nas outras linguagens, python tem suas formas de interpolar valores:
```Python
# Formato Clássico
print('Nome: %s Idade: %d' % (nome, idade))

# Recomendado para Python < 3.6
print('Nome: {0} Idade: {1}'.format(nome, idade))

# Formato mais atual para Python >= 3.6
print(f'Nome: {nome} Idade{idade} {2**8+1}')

# Exemplo prático
from String import Template
s = Template('Nome $n Idade $i')
print(s.substitute(n=nome, i=idade))
```

</details>

### 🧩 Seção 7: Estruturas de Controle
Nesta seção do curso, foi nos apresentado as estruturas de controle IF-ELSE, WHILE, FOR, SWITCH(simulado) e MATCH-CASE, além de bibliotecas como `random`.

<details><summary style="font-weight:bold">Estrutura de Condição</summary>

```python
# IF-ELSE

    if condicao:
        codigo
# OU
    if condicao:
        codigo
    else:
        outro_codigo
# OU

    if condicao1:
        codigo1
    elif condicao2:
        codigo2
    else:
        codigo3
```
```python
# MATCH-CASE
match variavel:
    case condicao1:
        codigo_case_1
    case condicao2:
        codigo_case_2
    case _:
        codigo_default

```

</details>

<details><summary style="font-weight:bold">Estrutura de Repetição</summary>

```python
# LAÇO WHILE
    while condicao:
        codig

# LAÇO FOR
    for i in range(1, 10, 2): #vai do 1 ao 10, pula 2 em 2
        print(i)
        break    # controle de loop
        continue # controle de loop
        pass     # controle de loop
```
</details>

<details><summary style="font-weight:bold">Estrutura de Exceções</summary>

```python
# TRY/EXCEPT/FINALLY
    try:
        x=int("abc")
    except ValueError:
        print("erro")
    finally: #opcional
        print("sempre executa")
```

</details>

### 📂 Seção 9: Manipulação de Arquivos
Nesta seção foi apresentado-nos formas de manipular um arquivo `.CSV`, desde à criação até à leitura, trazendo técnicas de leitura como o Streaming, onde python lê os arquivos sobre demanda ao invés de ler por completo para então executar, reduzindo o consumo de memória. Dessa forma, fizemos a leitura e manipulação com `WITH`, `TRY/EXCEPT/FINNALLY`, com variável carregando localmente os dados e com a manipulação ocorrendo enquanto o arquivo estava em `open().`
Houve também a utilização de funções nativas como `split()`, `strip()` e `csv.reader()`.

### ⚡ Seção 10: Comprehension
- List Comprehension:
    É uma sintaxe que cria lista de forma mais concisa e rápida a  partir de uma única linha.
    ```python
    [ expressão for item in lista if condicional ]
    ```
- Generator Comprehension:
    Também foi citado sobre os `Generators` que têm uma sintaxe parecida, porém que traz grande diferença no quesito desempenho, consumindo menos memória que o List Comprehension, pois sua geração é feita sob demanda.
    ```python
    ( expressão for item in lista if condicional )
    ```
- Dictionary Comprehension
    ```python
    { chave:valor_expressão for item in lista if condicional }
    ```


### 🔃 Seção 11: Funções
- Para as funções existem dois tipos de parâmetros: `Posicional` e `Nomeado`.
- Os parâmetros podem ser omitidos em determinados cenários sem que haja problemas.
- Para o uso das tuplas e dicionários em parâmetros usamos o `*`.
- As funções em python são tratadas como objeto e um objeto pode se comportar como uma função.
- Nesta seção utilizamos comandos como `assert` e a linguagem HTML. Além de conceitos como packing, unpacking, callable e o Design Pattern Decorator.

Durante as aulas vimos que é possível chamar funções dentro de funções, tornar funções Callable em Object, resolver o problema do parâmetro padrão mutável e aplicação do padrão de projeto Decorator. Ademais, além do `return`, podemos usar o `yield` em seu lugar seguido de uma numeração (`yield 1, yield 2, ...`). O `yield` diferentemente do return pausa a função ao invés de encerrá-la, tornando sua execução contínua e sob demanda, pois utiliza do conceito de Lazy Evaluation, podendo retornar mais de um valor e voltando à sua execução onde parou após feita uma nova demanda.

### 🧱 Seção 13: Programação Orientada à Objetos
Nesta seção vimos a definição de Classe e Objeto, do que são compostos e uma visão geral de POO, além dos seus principais pilares.
- Os 4 pilares de POO são: 
    - `Herança`: Capacidade de reusar código vindo de um tipo mais genérico e recebendo comportamento por herança pra um tipo mais específico.
    - `Polimorfismo (conceito DuckType)`: Capacidade de substituir tipos que se comportam do mesmo jeito. Muda um pouco de acordo com o tipo de linguagem que você utiliza e a forma como implementamos.
    - `Encapsulamento`: Capacidade de esconder os detalhes de implementação, tornando necessário somente conhecer a interface de comunicação e o que lhe dará como retorno.
    - `Abstração`: Saber extrair do mundo real o que de fato é relevante para o sistema.
Também foi mostrado diferente tipos de exemplos utilizando método construtor (`__init__`) e outros métodos como `__str__`, `__iter__`, `super()`, além de bibliotecas como `datetime`

### 🔁 Seção 15: Programação Funcional
Nesta seção estudamos sobre o paradigma da programação funcional e seus principais tópicos: 
- `First Class Functions`: funções que são tratadas como qualquer outro valor, são tratadas como um dado.
    <details><summary>Exemplo</summary>

    ```python
    def dobro(x):
        return x*2
    def quadrado(x):
        return x**2
    if __name__ == '__main__':
        # Retorna alternadamente o dobro ou quadrado nos números de 1 a 10
        funcs = [dobro, quadrado] * 5
        for func, numero in zip(funcs, range(1,11)):
            print(f'O {func.__name__} de {numero} é {func(numero)}')
    ```
    </details><br>
- `High Order Functions`: funções que recebem função como parâmetro e também pode ter como retorno uma função.
    <details><summary>Exemplo</summary>

    ```python
    from funcao_primeira_classe_import dobro, quadrado
    def processar(titulo, lista, funcao):
        print(f'Processando: {titulo}')
        for i in lista:
            print(i, '=>', funcao(i))
    if __name__=='__main':
        processar('Dobros de 1 a 10', range(1,11), dobro)
        processar('Quadrados de 1 a 10', range(1,11), quadrado)
    ```
    </details><br>
- `Anonymous Functions`: São funções não nomeadas (sem nome).
    <details><summary>Exemplo</summary>

    ```python
    # map, filter, sorted, reduce... todas são funções Anonymous.

    list(map(lambda x: x * 2, nums))

    list(filter(lambda x: x % 2 == 0, nums))

    pessoas = [('Ana', 25), ('João', 20)]
    sorted(pessoas, key=lambda p: p[1])

    reduce(lambda a, b: a + b, nums)
    ```
    </details><br>
- `Closure`: uma função que carrega junto com ela valores do escopo onde foi criada, mesmo depois desse escopo ter acabado
    <details><summary>Exemplo</summary>

    ```python
        def multiplicar(x):
            def calcular(y):
                return x*y                  # uso do valor fechado (closure)
            return calcular                 # conceito de alta ordem
        triplo = multiplicar(3)             # closure criada e armazena x=3
        print(f'triplo de 3 é {triplo(3)}') # triplo(3) == calcular(3)
        
    ```
    </details><br>
- `Recursion`: recursão é quando uma função chama ela mesma para resolver um problema menor até chegar num caso base.
    <details><summary>Exemplo</summary>

    ```python
    def fatorial(n):
    if n == 0:
        return 1      # caso base
    return n * fatorial(n - 1)
    ```
    </details><br>
- `Immutability`: imutabilidade é quando um objeto não pode ser alterado depois de criado. Se “mudou”, na real foi criado outro objeto. Devemos dar preferência para dados imutáveis, pois torna mais previsível.
    <details><summary>Exemplo</summary>

    ```python
    # int, float, str, tuple, frozenset são tipos imutáveis

    x = 10
    x = x + 1 # 10 não virou 11, um novo int foi criado. 
    ```
    </details><br>

- `Lazy Evaluation`: quando o código só é executado no momento em que o valor é realmente necessário, ou seja, sob demanda.
    <details><summary>Exemplo</summary>

    ```python
    # map(), filter(), range(), zip(), enumerate, iter(), generators são Lazy.

    def numeros():
        print("gerando 1")
        yield 1
        print("gerando 2")
        yield 2
    g = numeros()
    next(g) # Saída: gerando 1
    ```
    </details><br>

E também algumas funções úteis:
|Função| Utilidade| Exemplo|
|:-:|:-:|:-:|
|`zip()`| Junta duas listas em tuplas, seja dentro de uma lista ou uma tupla maior ou até mesmo um dicionário.
|`lambda`| Função anônima de uma linha onde há retorno implícito. Usada para criar funções rápidas e descartáveis sem def. Assim como uma função, lambda não se limita à apenas um parâmetro.| lambda parametros: expressao`lambda i: i**2`|
|`map()`| Função para mapear cada um dos elementos de uma lista para outros tipos de elementos em uma outra lista. Basicamente aplica outra função a cada elemento de um iterável e retorna um iterador lazy com os resultados.| `tuple(map(lambda i: i**2, tupla_1))`|
| `filter()`|É uma função que filtra elementos de um iterável, mantendo apenas os que fazem a função retornar True.| `pares = filter(lambda x: x % 2 == 0, nums)`
|`reduce()`|É uma função que reduz um iterável a um único valor, aplicando uma função acumuladora elemento por elemento. Necessário importar `functools` para usar.|`nums = [1, 2, 3, 4]`<br>`total = reduce(lambda a, b: a + b, nums)`|

Além disso, também foi discernido a diferença entre os paradigmas: <u>Linguagem Imperativa</u>, <u>Linguagem Orientada à Objetos</u>, <u>Linguagem Declarativa</u>, <u>Linguagem Funcional</u>, na qual é subtipo de declarativa.
- **Linguagem Imperativa** diz COMO fazer, num passo a passo, tendo como foco o controle do fluxo
    <details><summary>Exemplo</summary>

    ```python
    # Estilo receita de bolo
    nums = [1, 2, 3]
    soma = 0

    for n in nums:
        soma += n
    ```
    </details><br>
- **Linguagem Orientada à Objetos** foca em Objetos + Estado, mistura dados e comportamento, em suma.
    <details><summary>Exemplo</summary>

    ```python
    class Pessoa:
        def __init__(self, nome):
            self.nome = nome
    ```
    </details><br>
- **Linguagem Declarativa** você diz O QUE quer, não como, sendo de uma forma mais "verbosa" e expressivo. Tendo como foco os resultados e sendo um controle menos explícito.
    <details><summary>Exemplo</summary>
    
    ```python
    sum([1, 2, 3])
    ```
    </details><br>
- **Linguagem Funcional** é um subtipo do declarativo, tendo como foco funções. Funções de primeira classe, funções puras, imutabilidade, recursão, lazy e etc. Toda funcional é declarativa, no entanto, nem toda declarativa é funcional.
    <details><summary>Exemplo</summary>
    
    ```python
    reduce(lambda a, b: a + b, [1, 2, 3])
    # OU
    nums = [1, 2, 3]
    list(map(lambda x: x * 2, nums))
    ```
    </details>

### 🧪 Seção 17: Isolamento de Ambientes
Foi feita a explicação de como criar a pasta `.venv` e sua instalação.

# 👁‍🗨 Evidências
Não houve conteúdo didático que necessitasse de comprovação técnica.

# 🎯 Desafio da Sprint
Não houve desafio da Sprint.

# ✅ Certificados
Não houve cursos externos, apenas dentro da Compass Udemy.