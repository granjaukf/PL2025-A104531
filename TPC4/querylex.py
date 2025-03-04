# ------------------------------------------------------------
# querylex.py
#
# tokenizer for a query language (SPARQL)
# ------------------------------------------------------------
import ply.lex as lex
import re

# list of token names.
tokens = (
    'SELECT',
    'WHERE',
    'LIMIT',
    'VARIAVEL',
    'ID',
    'PONTO',
    'CA',
    'CF',
    'TAG',
    'STRING',
    'NUM',
    'DOISPONTOS',
    'COMMENT',
)

# Regular expression rules for tokens
def t_SELECT(t):
    r'select'
    t.type = 'SELECT'
    t.value = 'select'
    return t

def t_WHERE(t):
    r'where'
    t.type = 'WHERE'
    t.value = 'where'
    return t

def t_LIMIT(t):
    r'limit'
    t.type = 'LIMIT'
    t.value = 'limit'
    return t

t_VARIAVEL = r'\?[\w]+'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PONTO = r'\.'
t_CA = r'\{'
t_CF = r'\}'
t_TAG = r'@\w+'
t_STRING = r'".*?"'
t_NUM = r'\d+'
t_DOISPONTOS = r':'
t_COMMENT = r'#.*'
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(reflags=re.IGNORECASE)

def main():
    file = open("lextoken.txt", "w")
    data = """
    # DBPedia: obras de Chuck Berry
    
    SELECT ?nome ?desc WHERE {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
    } LIMIT 1000
    """
    lexer.input(data)
    for tok in lexer:
        print(tok, file=file)

if __name__ == "__main__":
    main()