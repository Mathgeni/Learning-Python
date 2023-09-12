from functools import reduce


class Binomial:
    """
    Class represents binomial expressions with ordering as Ax^n + Bx^(n-1) + ... + Cx + D.
    For determination coefficients A, B, ..., C, D use object[index] where index is index of coefficient
    if A, B, ..., C, D was a list. For example: index of A is 0, B is 1, etc.
    """

    def __init__(self, order=0):
        self.params = [0 for _ in range(order + 1)]

    def __setitem__(self, key, value):
        self.params[key] = value

    def __call__(self, x, *args, **kwargs):
        return reduce(lambda total, current: total + current[1] * x ** (len(self.params) - current[0]),
                      enumerate(self.params, 1), 0)

    def __str__(self):
        def func(expression):
            if expression[1]:
                return f'{expression[1]}*x^{len(self.params) - expression[0]}'
            return f'param{len(self.params) - expression[0]}*x^{len(self.params) - expression[0]}'

        formatted = map(func, enumerate(self.params, 1))
        return '+'.join(formatted)
