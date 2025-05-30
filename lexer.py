import re

TOKEN_SPEC = [
    ('NUMBER',   r'\d+'),
    ('STRING',   r'"[^"]*"'),
    ('IDENT',    r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('ASSIGN',   r'='),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('PRINT',    r'print'),
    ('LET',      r'let'),
    ('NEWLINE',  r'\n'),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.')
]

TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

def tokenize(code):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unbekanntes Symbol: {value}')
        else:
            tokens.append((kind, value))
    return tokens
