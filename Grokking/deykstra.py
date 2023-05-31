def find_lowest(costs: dict, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


graph = {
    'start': {'b': 5, 'a': 2},
    'b': {'c': 2, 'd': 4},
    'a': {'c': 7, 'b': 8},
    'd': {'finish': 2, 'c': 6},
    'c': {'finish': 1},
    'finish': {}
}

costs = {
    'a': 6,
    'b': 2,
    'c': float('inf'),
    'd': float('inf'),
    'finish': float('inf')
}

parents = {
    'a': 'start',
    'b': 'start',
    'start': None
}

processed = []
out = []

if __name__ == '__main__':
    node = find_lowest(costs, processed)
    while node is not None:
        cost = costs[node]
        for n in graph[node].keys():
            new_cost = cost + graph[node][n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest(costs, processed)

    node = 'finish'
    while node is not None:
        out.append(node)
        node = parents[node]

    print(' -> '.join(out))
