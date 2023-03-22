def gen(n):
    for i in range(n):
        yield i
    # Возвращается в следующем вызове next()
    # print('hello')


if __name__ == '__main__':
    g = gen(10)
    while True:
        try:
            print(next(g))
        except StopIteration:
            pass

