with open('input.txt', 'r', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as output:
    text = file.read()
    symbols = {}
    for c in text:
        if c not in [' ', '\n']:
            symbols[c] = symbols.get(c, 0) + 1
    symbols = {key: value for key, value in sorted(symbols.items(), key=lambda x: x[0])}
    maxvalue = max(symbols.values())
    keys = list(symbols.keys())
    out = [[' ' for _ in range(len(symbols))] for _ in range(maxvalue + 1)]
    for i in range(len(symbols)):
        for j in range(maxvalue - symbols[keys[i]], maxvalue + 1):
            if j == maxvalue:
                out[j][i] = keys[i]
            else:
                out[j][i] = '#'
    for line in out:
        for c in line:
            output.write(c)
        if line != out[-1]:
            output.write('\n')
