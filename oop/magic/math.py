class Distance(float):
    def __new__(cls, distance, unit):
        instance = super().__new__(cls, distance)
        instance.unit = unit
        return instance

    def __pos__(self):
        return self + Distance('1.0', self.unit)

    def __neg__(self):
        return self - Distance('1.0', self.unit)

    def __add__(self, other):
        if self.unit == other.unit:
            return Distance(float(self) + float(other), self.unit)
        return f'{self.unit} is not {other.unit}'


if __name__ == '__main__':
    home = Distance(10.254, 'km')
    print(home)  # distance 10.254
    print(+home)  # distance 11.254
    print(-home)  # distance 9.254
    print(round(home, ndigits=0))  # distance 10.0
    shop = Distance(1.432, 'miles')
    print(+shop)
    print(home + shop)
    mom = Distance(5.0, 'km')
    road = mom + home
    print(road)
