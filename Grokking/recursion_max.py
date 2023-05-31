def max_num(arr):
    a = arr[0]
    for i in range(1, len(arr)):
        if a < arr[i]:
            a = arr[i]
    return a


if __name__ == '__main__':
    l = range(20)
    print(max_num(l))