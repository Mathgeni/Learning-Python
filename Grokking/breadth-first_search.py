def need(name):
    return True if name.lower() == 'adam' else False


def path(person, arr, graph):
    out = [person]
    print(arr)
    while person != 'you':
        for i in arr:
            if i in graph and person in graph[i]:
                out.append(i)
                person = i
                break
    return '->'.join(out[::-1])


def search(graph, name):
    queue = []
    queue += graph[name]
    searched = [name]
    while queue:
        person = queue[0]
        del queue[0]
        if person not in searched:
            if need(person):
                return path(person, searched, graph)
            else:
                if person in graph:
                    queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    graph = {
        'you': ['alice', 'bob', 'clare'],
        'alice': ['peggie'],
        'bob': ['peggie', 'anuje'],
        'clare': ['johnny', 'huke'],
        'huke': ['adam', 'billy']
    }
    print(search(graph, 'you'))
