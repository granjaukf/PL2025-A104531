# PL 2024/25 - TPC 4

## Data
4 de março de 2025

## Autoria
- **Nome**: Rodrigo Miguel Granja Ferreira
- **Número mecanográfico**: A104531
<img src="../foto.jpg" alt="Minha Foto" width="200"/>

## Resumo
O TP3 consistiu na implementação de um programa em Python que constrói um analisador léxico para uma linguagem de query (SPARQL), permitindo escrever frases como:
```
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```
Neste TPC4, desenvolvi um analisador léxico utilizando duas abordagens diferentes: uma com a biblioteca PLY (Python Lex-Yacc) e outra com expressões regulares nativas do Python.

## Metodologia

### Abordagem 1: Implementação com PLY
Na primeira abordagem, utilizei a biblioteca PLY para construir o analisador léxico. Defini os tokens e as expressões regulares associadas a cada um deles. O lexer lê uma query de exemplo e gera os tokens correspondentes, que são depois escritos num ficheiro de saída.

Abaixo, mostro como a estrutura básica do código foi construída:

- **Tokens**: `SELECT`, `WHERE`, `VARIAVEL`, `ID`, `DOISPONTOS`, `PONTO`, `STRING`, `TAG`, `CA`, `CF`, `COMMENT`.
- **Função de erro**: O lexer possui uma função que lida com caracteres ilegais.
- **Leitura de entrada**: A query é processada e os tokens são gerados e escritos num ficheiro de saída.

### Abordagem 2: Implementação com Expressões Regulares

Na segunda abordagem, optei por utilizar as expressões regulares nativas do Python para construir o analisador léxico. A função `tokenize` processa o código de entrada e gera uma lista de tokens que são então exibidos na saída.

Aqui, a estrutura de tokens é definida com expressões regulares para cada tipo de token, como `SELECT`, `WHERE`, e `VARIAVEL`. A diferença principal em relação à primeira abordagem é que não se utiliza a biblioteca PLY, mas sim a funcionalidade de regex do Python.

## Resultados

Após processar a query de exemplo, o resultado da análise léxica foi armazenado num ficheiro de saída, onde cada linha representa um token identificado. Um exemplo dos tokens gerados para a query fornecida é o seguinte:
``` 
LexToken(COMMENT,'# DBPedia: obras de Chuck Berry',2,5)
LexToken(SELECT,'select',4,46)
LexToken(VARIAVEL,'?nome',4,53)
LexToken(VARIAVEL,'?desc',4,59)
LexToken(WHERE,'where',4,65)
LexToken(CA,'{',4,71)
LexToken(VARIAVEL,'?s',5,77)
LexToken(ID,'a',5,80)
LexToken(ID,'dbo',5,82)
LexToken(DOISPONTOS,':',5,85)
LexToken(ID,'MusicalArtist',5,86)
LexToken(PONTO,'.',5,99)
LexToken(VARIAVEL,'?s',6,105)
LexToken(ID,'foaf',6,108)
LexToken(DOISPONTOS,':',6,112)
LexToken(ID,'name',6,113)
LexToken(STRING,'"Chuck Berry"',6,118)
LexToken(TAG,'@en',6,131)
LexToken(PONTO,'.',6,135)
LexToken(VARIAVEL,'?w',7,141)
LexToken(ID,'dbo',7,144)
LexToken(DOISPONTOS,':',7,147)
LexToken(ID,'artist',7,148)
LexToken(VARIAVEL,'?s',7,155)
LexToken(PONTO,'.',7,157)
LexToken(VARIAVEL,'?w',8,163)
LexToken(ID,'foaf',8,166)
LexToken(DOISPONTOS,':',8,170)
LexToken(ID,'name',8,171)
LexToken(VARIAVEL,'?nome',8,176)
LexToken(PONTO,'.',8,181)
LexToken(VARIAVEL,'?w',9,187)
LexToken(ID,'dbo',9,190)
LexToken(DOISPONTOS,':',9,193)
LexToken(ID,'abstract',9,194)
LexToken(VARIAVEL,'?desc',9,203)
LexToken(CF,'}',10,213)
LexToken(LIMIT,'limit',10,215)
LexToken(NUM,'1000',10,221)

``` 

Cada token é descrito com o seu tipo, valor e a linha e coluna onde foi encontrado. Isso demonstra que tanto a implementação com PLY quanto a com expressões regulares conseguem processar corretamente a query de entrada, identificando os diversos componentes da linguagem SPARQL.

## Conclusão

Ambas as abordagens (PLY e expressões regulares) foram eficazes para implementar o analisador léxico, com a PLY oferecendo uma solução mais robusta e modular, enquanto a utilização de expressões regulares nativas do Python se mostrou uma alternativa simples e prática. O processo de análise léxica funcionou corretamente, gerando os tokens da query de exemplo conforme esperado. A escolha entre as duas abordagens depende das necessidades específicas do projeto, sendo a PLY mais adequada para casos mais complexos e a abordagem com regex mais direta e fácil de implementar.
