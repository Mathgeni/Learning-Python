class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} || {self.surname}'

    def __eq__(self, other):
        return self.name == other.surname and self.surname == other.surname

    def __hash__(self):
        return hash((self.name, self.surname))


if __name__ == '__main__':
    mom = Person('Sveta', 'Ivanova')
    me = Person('Nikita', 'Kanunnikov')
