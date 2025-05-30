def run(ast):
    env = {}

    for node in ast:
        if node[0] == 'let':
            env[node[1]] = node[2]
        elif node[0] == 'print':
            val = env.get(node[1], node[1])
            print(val.strip('"'))
