class CustomList:
    """
    Custom list class
    """

    def __init__(self, *values):
        if not values:
            self.values = []
        self.values = [value for value in values]

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return self.values[::-1]

    def __str__(self):
        return f'{self.values}'
