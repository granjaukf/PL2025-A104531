# PL 2024/25 - TPC 1

## Data
10 de fevereiro de 2025

## Autoria
- Nome: Rodrigo Miguel Granja Ferreira
- Número mecanográfico: A104531
<img src="../foto.jpg" alt="Minha Foto" width="200"/>

## Resumo 
O TP1 consistiu na implementação de um programa em Python que:
1. Some todas as sequências de dígitos num texto;
2. Sempre que encontrar a string `Off`, em qualquer combinação de maiúsculas e minúsculas, o comportamento de soma é desligado;
3. Sempre que encontrar a string `On`, em qualquer combinação de maiúsculas e minúsculas, o comportamento de soma é ligado;
4. Sempre que encontrar o caráter `=`, o resultado da soma é colocado na saída.

A função `adder` foi desenvolvida para percorrer o texto, identificar palavras reservadas (=, On, Off) e literais numéricos, controlar a soma e gerar resultados conforme solicitado. Os testes foram realizados com diferentes combinações de entradas para verificar o comportamento do programa em situações variadas.

## Metodologia

A solução para o problema proposto foi desenvolvida utilizando uma abordagem simples e eficiente. O programa foi implementado em Python e segue uma abordagem de processamento sequencial do texto, percorrendo-o caractere a caractere. O fluxo de controlo foi baseado na deteção de palavras reservadas (=, On, Off) e literais numéricos. Aqui estão os detalhes sobre como a implementação foi organizada:

1. **Analisador Léxico**: O programa percorre o texto e identifica sequências de dígitos e palavras reservadas. Quando encontra uma sequência de dígitos, ela é acumulada em uma variável que posteriormente é convertida para um número inteiro e somada. A palavra `Off` desativa a soma, e a palavra `On` ativa novamente a soma.

2. **Controlo de Estado**: Foi implementado um mecanismo de controlo de estado utilizando uma variável booleana (`adderOn`) que mantém o estado da soma (se está ligada ou desligada). Toda vez que o programa encontra `Off`, a soma é desativada, e quando encontra `On`, ela é ativada novamente.

3. **Output**: Quando o caractere `=` é encontrado no texto, o valor atual da soma é impresso. O programa continua a processar até ao final do texto, respeitando todas as ativações e as desativações de soma.

4. **Validação e Testes**: O código foi testado com diversos exemplos de input, variando as combinações de números, palavras reservadas e caracteres especiais, para garantir que o comportamento do programa fosse o esperado. Todos os testes foram realizados manualmente e os resultados foram comparados com a saída esperada.

Essa estrutura simples foi suficiente para resolver o problema proposto sem a necessidade de recursos avançados como expressões regulares, mantendo o código mais legível e eficiente.

## Resultados

O programa desenvolvido foi testado com vários inputs e os resultados obtidos confirmaram que o comportamento de soma e o controle de ativação/desativação funcionam corretamente. Os testes foram realizados para garantir que os comandos `On` e `Off` sejam respeitados, e que a soma seja calculada conforme esperado, com os resultados impressos corretamente quando o caractere `=` é encontrado. Além disso, a implementação em Python foi otimizada e validada.
