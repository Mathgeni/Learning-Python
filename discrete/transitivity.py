import random


x = 4
y = 4
array = [[random.randint(0, 1) for i in range(x)] for j in range(y)]
rel = {(i, j) for i, elem in enumerate(array) for j, val in enumerate(elem) if array[i][j] == 1}
def is_transitive(rel):
    seconds_elements = {b for (a, b) in rel}
    for (a, b) in rel:
        for c in seconds_elements:
            if (b, c) in rel and (a, c) not in rel:
                return False
    return True


print(is_transitive(rel))
