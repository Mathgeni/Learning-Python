import random


def binary(arr, elem):
    i = 0
    left = 0
    right = len(arr) - 1
    middle = (left + right) // 2
    i += middle
    if arr[middle] == elem:
        return i
    elif arr[middle] < elem:
        return binary(arr[middle + 1:], elem)
    else:
        return binary(arr[:middle], elem)


if __name__ == '__main__':
    l = [random.randint(1, 100) for _ in range(10)]
    l.sort()
    print(l)
    elem = random.choice(l)
    print(elem)
    print(binary(l, elem))
