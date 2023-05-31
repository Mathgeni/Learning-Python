def table(scores: dict[str], capacity: int):
    """
    Функция принимает словарь данных с определенным весом
    находит максимальную стоимость рюкзака с максимальной
    вместимостью
    """
    min_cap = float('inf')
    for key, value in scores.items():
        if value[0] < min_cap:
            min_cap = value[0]
    cell = [[0 for _ in range(0, capacity, min_cap)] for _ in range(len(scores))]
    for i, key in enumerate(scores):
        value = scores[key]
        for j in range(len(cell[i])):
            if i == 0:
                if value[0] - 1 <= j:
                    cell[i][j] = value[1]
            else:
                if j - value[0] + 1 <= 0:
                    cell[i][j] = cell[i - 1][j] if cell[i - 1][j] > value[1] or value[0] - 1 > j else value[1]
                else:
                    if cell[i - 1][j] > value[1] + cell[i - 1][j - value[0]]:
                        cell[i][j] = cell[i - 1][j]
                    else:
                        cell[i][j] = value[1] + cell[i - 1][j - value[0]]
    return cell


if __name__ == '__main__':
    print(table({'water': (3, 10), 'book': (1, 3), 'food': (2, 9), 'jacket': (2, 5), 'camera': (1, 6)}, 6))
