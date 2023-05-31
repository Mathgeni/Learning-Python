def sum1(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


if __name__ == '__main__':
    l = [i for i in range(1, 5)]
    print(sum1(l))