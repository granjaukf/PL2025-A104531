# expr_anasin.py
# 2025-03-17 by rmg
# ----------------------
from expr_analex import lexer

prox_simb = ('Erro', '', 0, 0)

# R com maior precedência para * e suporte a parênteses
# Exp -> Term Exp'
# Exp' -> ('+' | '-') Term Exp' |
# Term -> Factor Term'
# Term' -> ('*') Factor Term' | 
# Factor -> '(' Exp ')' | num

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

# Factor -> num      
def rec_Factor():
    global prox_simb
    if prox_simb.type == 'NUM':
        valor = int(prox_simb.value)
        prox_simb = lexer.token()
        return valor
    elif prox_simb.type == 'LPAREN':
        prox_simb = lexer.token()
        valor = rec_Exp()
        if prox_simb.type == 'RPAREN':
            prox_simb = lexer.token()
            return valor
        else:
            parserError(prox_simb)
            return None
    
# Term' -> ('*') Factor Term' | 
def rec_TermP(valor_esq):
    global prox_simb
    while prox_simb and prox_simb.type == 'TIMES':
        prox_simb = lexer.token()
        valor_dir = rec_Factor()
        valor_esq *= valor_dir 
    
    return valor_esq

# Term -> Factor Term'
def rec_Term():
    valor_esq = rec_Factor()
    return rec_TermP(valor_esq)

# Exp' -> ('+' | '-') Term Exp' |
def rec_ExpP(valor_esq):
    global prox_simb
    while prox_simb and prox_simb.type in ('PLUS','MINUS'):
        op = prox_simb.type
        prox_simb = lexer.token()
        valor_dir = rec_Term()
        if op == 'PLUS':
            valor_esq += valor_dir
        else:
            valor_esq -= valor_dir
    return valor_esq

# Exp -> Term Exp'
def rec_Exp():
    valor_esq = rec_Term()
    return rec_ExpP(valor_esq)

def rec_Parser(expr):
    global prox_simb
    lexer.input(expr)
    prox_simb = lexer.token()
    resultado = rec_Exp()
    return resultado
    
    
        