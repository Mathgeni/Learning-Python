import random


def binary_search(sorted_list, elem):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        middle = (left + right) // 2
        if sorted_list[middle] == elem:
            return middle
        if sorted_list[middle] < elem:
            left = middle + 1
        else:
            right = middle - 1
    return None


if __name__ == '__main__':
    l = [random.randint(1, 500) for _ in range(50)]
    l.sort()
    print(l)
    elem = random.choice(l)
    print(elem)
    print(binary_search(l, elem))
