from functools import reduce
# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
#            93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27,
#            57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29,
#            88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
# print(*list(map(lambda x: x // 2 if x % 2 == 0 else x, filter(lambda x: x % 2 == 0 or x % 2 != 0 and x < 47, numbers))))


# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
#         (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
#         (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
# data = sorted(data, key=lambda x: x[1][-1], reverse=True)
#
# for i in data:
#     print(f'{i[1]}: {i[0]}')
#

# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
# 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец',
# 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#
# data1 = sorted((data), key=lambda x: (len(x), x))
# print(*data1)
# data2 = sorted(sorted(data), key=len)
# print(*data2)


def evaluate(coefs, x):
    y = list(map(lambda k, z: k * z, coefs, [x ** i for i in range(len(coefs) - 1, -1, -1)]))
    return reduce(lambda n, m: m + n, y, 0)


k = [int(i) for i in input().split()]

x = int(input())

print(evaluate(k, x))
