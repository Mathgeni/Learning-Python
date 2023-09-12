class Word(str):
    def __new__(cls, word):
        return super().__new__(cls, word)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)


if __name__ == '__main__':
    bar = Word('bar')
    foo = Word('foo')
    print(bar > foo)
    print(bar == foo)