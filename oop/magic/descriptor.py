class Second:
    def __init__(self, seconds=0):
        self.seconds = seconds

    def __get__(self, instance, owner):
        return self.seconds

    def __set__(self, instance, value):
        self.seconds = value


class Minute:
    def __init__(self, minutes=0):
        self.minutes = minutes

    def __get__(self, instance, owner):
        return self.minutes

    def __set__(self, instance, value):
        self.minutes = value


class Hour:
    def __init__(self, hours=0):
        self.hours = hours

    def __get__(self, instance, owner):
        return self.hours

    def __set__(self, instance, value):
        self.hours = value


class Time:
    seconds = Second()
    minutes = Minute()
    hours = Hour()
