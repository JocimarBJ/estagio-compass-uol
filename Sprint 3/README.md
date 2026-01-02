# 📝 Resumo
 
|<h3>🔍ÍNDICE</h3>|
|------------------|
| [🧠 Competências Aplicadas](#-competências-aplicadas) |

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

### Seção 4: Executando Código Python
Podemos executar um código python utilizando o interpretador próprio da linguagem através de linhas de comando no terminal. Também através do Jupyter ou no VSCode.

### Seção 5: Fundamentos de Python
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
No entanto, por ser uma linguagem fortemente tipada e dinâmica, significa que o Python sempre estará ciente sobre a existência dos tipos e faz a validação se podemos ou não fazer determinadas operações, no entanto não irá bloquear você de, a partir de uma única variável, colocar diferentes tipos nessa variável.
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
    Compara os bits das variáveis entre si e funciona como um operador lógico, no entanto é necessário ter cuidado ao usar. Quando precisarmos usar operadores lógicos não é recomendado usá-los.
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

As funções `type()`, `help()`, `print()` e etc, fazem parte do Builtins.
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

### Seção 7: Estruturas de Controle
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