from lexer import tokenize
from parser import parse
from runtime import run

if __name__ == '__main__':
    with open('tests/test_hello.lumen', 'r') as f:
        code = f.read()
    tokens = tokenize(code)
    ast = parse(tokens)
    run(ast)
