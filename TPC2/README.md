# PL 2024/25 - TPC 2

## Data
19 de fevereiro de 2025

## Autoria
- Nome: Rodrigo Miguel Granja Ferreira
- Número mecanográfico: A104531
<img src="../foto.jpg" alt="Minha Foto" width="200"/>

## Resumo 
O TP2 consistiu na implementação de um programa em Python que exigia a análise de um dataset de obras musicais. Para isso, é necessário ler o dataset e preocessá-lo e criar alguns resultados, nomeadamente:
1. Lista ordenada alfabeticamente dos compositores musicais;
2. Distribuição das obras por período: quantas obras catalogadas em cada período;
3. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.

**Nota: Neste TPC, é proibido usar o módulo CSV do Python, uma vez para nos obrigar a ter a prática de conhecimentos de expressões regulares**

A função `parse` usa uma expressão regular para extrair as informações dos dados, como `nome da obra`, `compositor`, `ano de criação`, `período`, etc.

A função `process_data` organiza os dados em três formas distintas: uma lista dos compositores, a distribuição das obras por período, e um dicionário associando cada período a seus títulos de obras.

## Metodologia
Para implementar o programa que processa o dataset de obras musicais, utilizou-se a pipeline clássica de processamento de linguagens:

- Analisador Léxico: Através de uma expressão regular, os lexemas (valores do CSV) são extraídos e armazenados em dicionários com os atributos das obras musicais (nome, compositor, ano, etc.).

- Analisador Sintático: Os dados extraídos são organizados em estruturas adequadas, como listas ordenadas e dicionários, para facilitar as interrogações (compositores, distribuição por períodos, etc.).

- Analisador Semântico: A execução das interrogações é realizada com base nos dados organizados, gerando as saídas requeridas pelo problema.

1. A função `parse` utiliza a seguinte expresão regular para extrair os dados de cada linha do ficheiro:

`([^;]+);\s*"{0,3}([\s\S]*?)"{0,3}\s*;(\d+);([^;]+);([^;]+);(\d{2}:\d{2}:\d{2});(O\d+)`

- `([^;]+)` captura qualquer sequência de caracteres, exceto o ponto e vírgula, o que representa o `nome da obra`,`periodo` e `compositor`.

- `([\s\S]*?)` captura o campo de descrição, o que permite espaços e mudanças de linha, entre aspas opcionais. O `{0,3}` é para incluir o caso de começar com três aspas, pois foi um ponto que tive de acrescentar que inicialmente não estava a ter isso em conta.

- `(\d{2}:\d{2}:\d{2})` captura a duração no formato hh:mm:ss.

- `(O\d+)` captura o identificador único da obra.

A função `finditer` é utilizada em vez de `findall` para retornar um iterador de objetos match, o que facilita acessar e processar cada match individualmente. É util, porque oferece mais controlo sobre o processamento e permite acessar cada grupo de captura de forma mais eficiente, sem precsisar armazenar todos os resultados na memória de uma vez (como o `findall` faria). O `match.groups()` é usado para obter as partes capturadas pela expressão regular, que são então armazenadas num `dicionário`.

Depois, em relação ao processamento dos dados, foi feita a ordenação dos compositores em ordem alfabética, sendo algo trivial. Conta o número de obras por período utilizando um `defaultdict`. Por último, organiza e ordena alfabeticamente os títulos das obras por período.

A `main` lê o ficheiro, chama o parse para extrair os dados e faz de seguida o processamento. Os resultados são escritos no ficheiro `resultados.txt`.


## Resultados

O programa foi testado com com o ficheiro CSV, e os resultados confirmaram que a expressão regular implementada conseguiu processar corretamente os dados. Os lexemas foram identificados conforme esperado, incluindo textos entre aspas e sequências sem aspas. A saída foi gerada de acordo com os requisitos, com a lista ordenada dos compositores, a distribuição das obras por período e os títulos das obras organizados por período.
