print(all([True, True, True]))     #  возвращает True, так как все значения списка равны True

print(any([False, True, False]))       #  возвращает True, так как есть хотя бы один элемент, равный True

colors = ['red', 'green', 'blue']
for index, item in enumerate(colors):
    print(index, item)


result = zip(numbers, words, romans)