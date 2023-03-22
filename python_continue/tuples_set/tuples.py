# Перевод в лист
number_tuple = (1, 2, 3, 4, 5)
number_list = list(number_tuple)
print(number_list)

# Перевод в кортеж
str_list = ['один', 'два', 'три']
str_tuple = tuple(str_list)

# Распаковка
colors = ('red', 'green', 'blue', 'cyan')
a, b, c, d = colors

# Разделение
s1 = 'abc-de'.partition('-')
('abc', '-', 'de')

# f string
a = safd
print(f'{a:<4}')