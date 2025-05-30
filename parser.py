def parse(tokens):
    ast = []
    i = 0

    while i < len(tokens):
        token = tokens[i]
        if token[0] == 'LET':
            ident = tokens[i+1][1]
            value = tokens[i+3][1]
            ast.append(('let', ident, value))
            i += 4
        elif token[0] == 'PRINT':
            value = tokens[i+1][1]
            ast.append(('print', value))
            i += 2
        else:
            raise SyntaxError(f'Unerwartetes Token: {token}')
    return ast
