def pascal_triangle(n: int) -> list:
    triangle = [1]
    if n == 1:
        return triangle
    for _ in range(n):
        triangle = [sum(x) for x in zip([0] + triangle, triangle + [0])]
    return triangle


def expand(expr):
    func, power = expr.split('^')
    power = int(power)
    if power == 0:
        return '1'
    elif power == 1:
        return func[func.find('(') + 1: func.find(')')]
    if '+' in func:
        ax = func[func.find('(') + 1:func.find('+')]
        b = int(func[func.find('+'):func.find(')')])
    else:
        ax = func[func.find('(') + 1:func.find('-')] if func.find('-') != 1 else (
            func[func.find('-'):func.find('-', func.find('-') + 1)])
        b = int(func[func.find('-'):func.find(')')]) if func.find('-') != 1 else (
            int(func[func.find('-', func.find('-') + 1): func.find(')')]))
    if len(ax) == 1:
        a = 1
        x = ax[-1]
    elif len(ax) == 2 and ax[0] == '-':
        a = -1
        x = ax[-1]
    else:
        a, x = int(ax[:-1]), ax[-1]
    polynom = pascal_triangle(power)
    for i in range(len(polynom)):
        polynom[i] = str(polynom[i] * a ** (power - i) * b ** i) + f'{x}^{power - i}'
        item = polynom[i]
        if item[-1] == '0':
            polynom[i] = item[:item.find(x)]
        elif item[-1] == '1':
            polynom[i] = item[:item.find('^')]
        elif item[0] == '1' and item[1] == x:
            polynom[i] = item[1:]
        elif item[0] == '-' and item[1] == '1' and item[2] == x:
            polynom[i] = '-' + item[2:]
    out = ''
    for i in polynom:
        if i[0] == '-':
            out += i
        elif i[0] == '0':
            continue
        else:
            out += '+' + i
    return out[1:] if out[0] == '+' else out


if __name__ == '__main__':
    print(expand('(-y+14)^5'))
