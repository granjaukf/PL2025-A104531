# PL 2024/25 - TPC 3

## Data
24 de fevereiro de 2025

## Autoria
- Nome: Rodrigo Miguel Granja Ferreira
- Número mecanográfico: A104531
<img src="../foto.jpg" alt="Minha Foto" width="200"/>

## Resumo 
O TP2 consistiu na implementação de um programa em Python que converte de Markdown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet.

O programa inclui várias funções para converter diferentes elementos de Markdown para HTML:

- `markdownCabecalho`: Converte cabeçalhos Markdown (`#`, `##`, `###`) para tags HTML (`<h1>`, `<h2>`, `<h3>`).
- `markdownBold`: Converte texto em negrito (`**texto**`) para tags HTML (`<b>texto</b>`).
- `markdownItalic`: Converte texto em itálico (`*texto*`) para tags HTML (`<i>texto</i>`).
- `markdownLink`: Converte links Markdown (`[texto](link)`) para tags HTML (`<a href="link">texto</a>`).
- `markdownImagem`: Converte imagens Markdown (`![texto](link)`) para tags HTML (`<img src="link" alt="texto"/>`).
- `markdownListaNumerada`: Converte listas numeradas Markdown para listas ordenadas HTML (`<ol><li>item</li></ol>`).

A função `main` lê exemplos de Markdown, aplica as funções de conversão e escreve os resultados num ficheiro `resultados.txt`.

## Metodologia

Para a implementação do conversor de Markdown para HTML, segui os seguintes passos:

1. **Análise da Sintaxe Markdown**: Estudei a "Basic Syntax" da Cheat Sheet para identificar os elementos que precisavam ser convertidos.
2. **Desenvolvimento das Funções de Conversão**: Implementei funções específicas para converter cada elemento Markdown para o seu equivalente em HTML. Para isso, utilizei a função `re.sub` da biblioteca `re` (expressões regulares) do Python, que permite substituir padrões de texto de forma eficiente. Utilizei `grupos nomeados` nas expressões regulares para capturar partes específicas do texto a ser convertido. O uso de grupos nomeados foi determinante na resolução do problema porque permitiu identificar e substituir de forma precisa as partes do texto que correspondiam aos elementos Markdown, facilitando a conversão para HTML.
    - **`markdownCabecalho`**: Utiliza `re.sub` para converter cabeçalhos Markdown (`#`, `##`, `###`) para tags HTML (`<h1>`, `<h2>`, `<h3>`). A expressão regular `^(#{1,3})\s*(.*)$` captura os cabeçalhos e a função lambda substitui pelo HTML correspondente.
    - **`markdownBold`**: Converte texto em negrito (`**texto**`) para tags HTML (`<b>texto</b>`) usando a expressão regular `\*\*(?P<bold>.*?)\*\*`.
    - **`markdownItalic`**: Converte texto em itálico (`*texto*`) para tags HTML (`<i>texto</i>`) com a expressão regular `\*(?P<italic>.*?)\*`.
    - **`markdownLink`**: Converte links Markdown (`[texto](link)`) para tags HTML (`<a href="link">texto</a>`) utilizando a expressão regular `\[(?P<texto>.*?)\]\((?P<link>.*?)\)`.
    - **`markdownImagem`**: Converte imagens Markdown (`![texto](link)`) para tags HTML (`<img src="link" alt="texto"/>`) com a expressão regular `!\[(?P<texto>.*?)\]\((?P<link>.*?)\)`.
    - **`markdownListaNumerada`**: Converte listas numeradas Markdown para listas ordenadas HTML (`<ol><li>item</li></ol>`) utilizando uma função auxiliar `list_replacer` e a expressão regular `(?P<items>(?:^\d+\..*\n?)+)`.
3. **Testes Unitários**: Criei exemplos de Markdown para testar cada função individualmente e garantir que a conversão estava correta.
4. **Integração das Funções**: Desenvolvi a função `main` para integrar todas as funções de conversão e aplicar aos exemplos de Markdown.
5. **Geração do Ficheiro de Resultados**: A função `main` escreve os resultados das conversões num ficheiro `resultados.txt` para validação final.

## Resultados

Os resultados das conversões de Markdown para HTML são apresentados abaixo:

```plaintext
Conversão do cabeçalho: <h1>Exemplo</h1>
-------------------------------------
Conversão bold: Este é um <b>exemplo</b>
-------------------------------------
Conversão italic: Este é um <i>exemplo</i>
-------------------------------------
Conversão imagem: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/>
-------------------------------------
Conversão link: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
-------------------------------------
Conversão da lista numerada:
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

Os resultados demonstram que o programa é capaz de converter corretamente os elementos de Markdown para HTML, conforme especificado na "Basic Syntax" da Cheat Sheet.
