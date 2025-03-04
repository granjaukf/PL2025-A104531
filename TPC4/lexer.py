import sys
import re

def tokenize(code):
    tokens = []
    token_specification = [
        ('SELECT', r'SELECT'),
        ('WHERE', r'WHERE'),
        ('LIMIT', r'LIMIT'),
        ('VARIAVEL', r'\?[\w]+'),
        ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('PONTO', r'\.'),
        ('CA', r'\{'),
        ('CF', r'\}'),
        ('TAG', r'@\w+'),
        ('STRING', r'"[^\n"]*"'),
        ('NUM', r'\d+'),
        ('DOISPONTOS', r':'),
        ('COMMENT', r'#.*'),  # Novo token para comentários
        ('SKIP', r'[ \t]+'),
        ('NEWLINE', r'\n'),
    ]
    
    tok_regex = '|'.join(f'(?P<{id}>{expreg})' for id, expreg in token_specification)
    
    linha = 1
    for match in re.finditer(tok_regex, code, re.IGNORECASE):
        tipo = match.lastgroup
        valor = match.group(tipo)
        
        if tipo == 'SKIP': 
            continue
        
        if tipo == 'NEWLINE': 
            linha += 1
            continue
        else:
            tokens.append((tipo, valor, linha, match.span()))
    
    return tokens

def main():
    input_text = sys.stdin.read()
    tokens = tokenize(input_text)
    
    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()
