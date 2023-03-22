def decogen(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return inner


def average():
    count = 0
    summ = 0
    avg = 0

    while True:
        try:
            x = yield
        except StopIteration:
            print('Done!!!')
            break
        else:
            count += 1
            summ += x
            avg = round(summ / count, 2)

    return avg      # Возвращается, когда while прекращается.


@decogen
def delegator(g):
    result = yield from g       # yield from == StopIteration.value (return avg)
    print(result)
