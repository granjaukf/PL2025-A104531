# PL 2024/25 - TPC 5

## Data
**10 de março de 2025**

## Autoria
- **Nome:** Rodrigo Miguel Granja Ferreira  
- **Número mecanográfico:** A104531  
<img src="../foto.jpg" alt="Minha Foto" width="200"/>

## Resumo
O TPC5 consistiu na implementação de uma máquina de vending em Python, utilizando a biblioteca **PLY (Python Lex-Yacc)** para processar comandos. A máquina gerencia um stock de produtos e permite ao utilizador interagir através dos comandos **LISTAR, MOEDA, SELECIONAR, ADICIONAR e SAIR**.

**NOTA:** É necessário a instalação da biblioteca `tabulate: pip install tabulate`

## Implementação
### Estrutura do Stock
```python
stock = {
    "A23": ("água 0.5L", 10, 0.7),
    "B45": ("refrigerante 0.33L", 5, 1.20),
    "C12": ("batatas fritas", 8, 1.50),
}
```
### Tokens e Funções
- **LISTAR:** Mostra os produtos disponíveis.
- **MOEDA:** Processa moedas inseridas e atualiza o saldo.
- **SELECIONAR:** Permite a compra de um produto, verificando saldo e stock.
- **ADICIONAR:** Acrescenta stock a um produto.
- **SAIR:** Encerra o programa e devolve troco.

## Exemplos de Comandos
**Listar Produtos:**
```shell
>> LISTAR
cod  nome                 quantidade  preço
----  -------------------  -----------  ------
A23  água 0.5L            10           0.70
B45  refrigerante 0.33L   5            1.20
C12  batatas fritas       8            1.50
```

**Inserir Moedas e Comprar Produto:**
```shell
>> MOEDA 1e, 20c, 5c
Saldo = 1e25c
>> SELECIONAR A23
Pode retirar o produto dispensado "água 0.5L"
Saldo = 55c
```

**Adicionar Stock:**
```shell
>> ADICIONAR A23 5
maq: Quantidade do produto água 0.5L atualizada para 15.
```

**Sair e Devolver Troco:**
```shell
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c, 2x 2c.
maq: Até à próxima!
```

## Conclusão
A máquina de vending foi implementada com sucesso utilizando **PLY**. O programa processa comandos, gere stock e transações de forma modular e eficiente, permitindo futuras expansões de funcionalidades.
