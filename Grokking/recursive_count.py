def count(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + count(arr[1:])


if __name__ == '__main__':
    l = range(10)
    print(count(l))