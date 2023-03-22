# Методы словарей
a.keys()            # список ключей a
a.values()          # список значений a
a.items()           # кортежи пар a
c.get(a, b)         # возвращает значение по ключу а, б - если ключа нет
a.update(b)         # конкатенация a и b
a.setdefault(b, c)  # добавляет ключ б, если не было и с если, не было значения ранее



# Добавляет значение в квадрате для списка с ключом и
result = {}
for i in range(1, 16):
    result[i] = result.get(i, i ** 2)
print(result)

# zip
keys = ['name', 'age', 'job']
values = ['Timur', 28, 'Teacher']

info = dict(zip(keys, values))

# Считает количество букв в текст
text = 'footballcyberpunkextraterritorialityconversationalistblocko' \
       'phthalmoscopicinterdependencemamauserfff'
result = {}
for c in text:
    result[c] = result.get(c, 0) + 1

sentences = [[i.lower().strip('.,!?:;-') for i in input().split()],
         [i.lower().strip('.,!?:;-') for i in input().split()] ]

# Прикольный способ
i = 0
dcts = ({}, {})
for d in dcts:
    for word in sentences[i]:
        for c in word:
            d[c] = d.get(c, 0) + 1
    i += 1
print(('NO', 'YES')[dcts[0] == dcts[1]])

# Подается строка, делится на 2 через пробел, в словарь с ключом а создается значение б, и наоборот
words = {}
for _ in range(int(input())):
    a, b = input().split()
    words[a], words[b] = b, a
print(words[input()])