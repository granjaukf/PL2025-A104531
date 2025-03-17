# expr_analex.py
# 2025-03-17 by rmg
# ----------------------
import ply.lex as lex

tokens = ('NUM','PLUS','MINUS','TIMES')

t_NUM = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t '

def t_error(t):
    print('Caráter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)
    
lexer = lex.lex()
