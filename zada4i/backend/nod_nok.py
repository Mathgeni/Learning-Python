def main():
    x, y = map(int, input().split())
    count = 0
    if y % x == 0:
        y //= x
        count = 0
        i = 2
        while i ** 2 <= y:
            if y % i == 0:
                count += 1
                while y % i == 0:
                    y //= i
            i += 1
        if y != 1:
            count += 1
        print(count * 2)
    else:
        print(count)



if __name__ == '__main__':
    main()