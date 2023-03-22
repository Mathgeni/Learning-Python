def decogen(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return inner


def gen():
    x = 'Hello'
    message = yield x
    print(message)


@decogen
def average():
    count = 0
    summ = 0
    avg = 0

    while True:
        try:
            x = yield avg
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            avg = round(summ / count, 2)
