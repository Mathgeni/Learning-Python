# Задание множества и распаковка
numbers = {1, 2, 3, 3, 4, 5, 1, 4}
nums = set(range(10))
print(*numbers, *nums, sep=' ')

# Распаковка
a, b, c = input().split()
if set(a) == set(b) == set(c):
    print('YES')
else:
    print('NO')

# Операции
.union() = |
.intersection() = &
.difference() = -
.symmetric_difference() = ^
.issuperset() = >=
.issubset() = <=
.isdisjoint() = нет общих элементов

# Добавление
my_set = set()
for i in range(10):
    my_set.add(i ** 2)
print(my_set)