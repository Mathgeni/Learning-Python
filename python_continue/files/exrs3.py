with open(input()) as file:
    lines = [i.strip() for i in file.readlines()]
    out = []
    for i in range(1, len(lines)):
        line = lines[i]
        if 'def ' in line and lines[i - 1][0] == '#':
            out.append(line[4:line.index('(')])
    if len(out) == 0:
        print('Best Programming Team')
        print(*out, sep='\n')
    else:
        print(*out, sep='\n')

