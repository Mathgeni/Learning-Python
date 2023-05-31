def main():
    n = int(input())
    data = list(map(int, input().split()))
    s = set()
    for i in range(len(data)):
        if data[i] not in s:
            s.add(data[i])
            continue
        if data[i] in s:
            s.remove(data[i])
    return len(s)


if __name__ == '__main__':
    print(main())