graph = {
    'a': {'b': 5, 'c': 6},
    'b': {'o': 4, 'e': 3, 'c': 7},
    'c': {'d': 1},
    'd': {'e': 3, 'm': 8},
    'e': {'m': 2},
    'o': {'e': 1, 'm': 4},
    'm': {}
}
costs = {
    'b': 5,
    'c': 6,
    'd': float('inf'),
    'o': float('inf'),
    'e': float('inf'),
    'm': float('inf'),
}
parents = {
    'b': 'a',
    'c': 'a',
    'a': None
}
processed = []


def find_lowest(costs, processed):
    node = None
    lowest_cost = float('inf')
    for n in costs:
        cost = costs[n]
        if cost < lowest_cost and n not in processed:
            node = n
            lowest_cost = cost
    return node


def find_rout(parents):
    rout = []
    node = 'm'
    while node is not None:
        rout.append(node)
        node = parents[node]
    return ' -> '.join(rout)


def deykstra(graph, costs, processed):
    node = find_lowest(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest(costs, processed)
    return find_rout(parents)


if __name__ == '__main__':
    print(deykstra(graph, costs, processed))
