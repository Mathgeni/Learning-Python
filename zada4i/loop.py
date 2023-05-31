def dfs(graph, start, used, parents, cycle=False):
    used[start] = 1
    end = 0
    for node in graph[start]:
        if used[node] == 0:
            parents[node] = start
            result = dfs(graph, node, used, parents, cycle)
            if result:
                start, end, cycle = result
                break
        elif used[node] == 1 and node != parents[start]:
            cycle = True
            end = node
            break
    if cycle:
        return start, end, cycle
    else:
        used[start] = 2


def route(parents, end, start):
    out = [end]
    while end != start:
        end = parents[end]
        out.append(end)
    return out


def main():
    n = int(input())
    adjacency = [list(map(int, input().split())) for _ in range(n)]
    graph = dict(zip(range(1, n + 1), [[j + 1 for j in range(n) if adjacency[i][j]] for i in range(n)]))
    info = None
    flag = False
    i = 1
    used = [0 for _ in range(len(graph) + 1)]
    while not flag and i <= len(graph):
        if used[i] == 2:
            i += 1
            continue
        parents = [0 for _ in range(len(graph) + 1)]
        result = dfs(graph, i, used, parents, flag)
        if result is not None:
            info, flag = result[:-1], result[-1]
        i += 1
    return info, parents


if __name__ == '__main__':
    info, parents = main()
    if info:
        print('YES')
        result = route(parents, *info)
        print(len(result))
        print(*result)
    else:
        print('NO')
