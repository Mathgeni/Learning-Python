def get(d, key, var):
    if key == 'global' and var not in d[key]['vars']:
        return None
    elif var in d[key]['vars']:
        return key
    else:
        a = d[key]['parent']
        return get(d, a, var)


namespace = {'global': {'vars': set(), 'parent': None}}
out = []
for _ in range(int(input())):
    func, name, arg = input().split()
    if func == 'add':
        namespace[name]['vars'].add(arg)
    if func == 'create':
        scope = {'vars': set(), 'parent': arg}
        namespace[name] = scope
    if func == 'get':
        out.append(get(namespace, name, arg))

print(*out, sep='\n')

