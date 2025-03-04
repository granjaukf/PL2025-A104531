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
LexToken(COMMENT,'# DBPedia: obras de Chuck Berry',1,0)
LexToken(SELECT,'select',2,36)
LexToken(VARIAVEL,'?nome',2,43)
LexToken(VARIAVEL,'?desc',2,49)
LexToken(WHERE,'where',2,55)
LexToken(CA,'{',2,61)
LexToken(VARIAVEL,'?s',3,67)
LexToken(ID,'a',3,70)
LexToken(ID,'dbo',3,72)
LexToken(DOISPONTOS,':',3,75)
LexToken(ID,'MusicalArtist',3,76)
LexToken(PONTO,'.',3,89)
LexToken(VARIAVEL,'?s',4,95)
LexToken(ID,'foaf',4,98)
LexToken(DOISPONTOS,':',4,102)
LexToken(ID,'name',4,103)
LexToken(STRING,'"Chuck Berry"',4,108)
LexToken(TAG,'@en',4,121)
LexToken(PONTO,'.',4,125)
LexToken(VARIAVEL,'?w',5,131)
LexToken(ID,'dbo',5,134)
LexToken(DOISPONTOS,':',5,137)
LexToken(ID,'artist',5,138)
LexToken(VARIAVEL,'?s',5,145)
LexToken(PONTO,'.',5,147)
LexToken(VARIAVEL,'?w',6,153)
LexToken(ID,'foaf',6,156)
LexToken(DOISPONTOS,':',6,160)
LexToken(ID,'name',6,161)
LexToken(VARIAVEL,'?nome',6,166)
LexToken(PONTO,'.',6,171)
LexToken(VARIAVEL,'?w',7,177)
LexToken(ID,'dbo',7,180)
LexToken(DOISPONTOS,':',7,183)
LexToken(ID,'abstract',7,184)
LexToken(VARIAVEL,'?desc',7,193)
LexToken(CF,'}',8,203)
LexToken(LIMIT,'limit',8,205)
LexToken(NUM,'1000',8,211)

``` 

Cada token é descrito com o seu tipo, valor e a linha e coluna onde foi encontrado. Isso demonstra que tanto a implementação com PLY quanto a com expressões regulares conseguem processar corretamente a query de entrada, identificando os diversos componentes da linguagem SPARQL.

## Conclusão

Ambas as abordagens (PLY e expressões regulares) foram eficazes para implementar o analisador léxico, com a PLY oferecendo uma solução mais robusta e modular, enquanto a utilização de expressões regulares nativas do Python se mostrou uma alternativa simples e prática. O processo de análise léxica funcionou corretamente, gerando os tokens da query de exemplo conforme esperado. A escolha entre as duas abordagens depende das necessidades específicas do projeto, sendo a PLY mais adequada para casos mais complexos e a abordagem com regex mais direta e fácil de implementar.
