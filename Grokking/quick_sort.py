import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    elem = arr[middle]
    less = [i for i in arr if i < elem]
    greater = [i for i in arr if i > elem]
    return quick_sort(less) + [elem] + quick_sort(greater)


if __name__ == '__main__':
    l = [random.randint(1, 100) for _ in range(20)]
    print(l)
    print(quick_sort(l))
