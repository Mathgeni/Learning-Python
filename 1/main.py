# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')


#  Следующий урок
# num = int(input())
# print(num)
# print(num + 1)
# print(num + 2)


#  Целочисленное деление
#  % - остаток от деления, // - целочисленное деление


# a = int(input())
# b = int(input())
# print(a if a < b else b)


# Сложение положительных чисел
# a, b, c = int(input()), int(input()), int(input())
# if a < 0:
#     if b < 0:
#         if c < 0:
#             print("0")
#         else:
#             print(c)
#     else:
#         if c < 0:
#             print(b)
#         else:
#             print(b + c)
# else:
#     if b < 0:
#         if c < 0:
#             print(a)
#         else:
#             print(a + c)
#     else:
#         if c < 0:
#             print(a + b)
#         else:
#             print(a + b + c)


# a, b, c = int(input()), int(input()), int(input())
# total = 0
# if a > 0:
#     total = total + a
# if b > 0:
#     total = total + b
# if c > 0:
#     total = total + c
# print(total)


# Ход короля
# x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())
# if not (not (abs(x_1 - x_2) == 1 and y_1 == y_2) and not (abs(y_1 - y_2) == 1 and x_1 == x_2) and not (
#         abs(y_1 - y_2) == 1 and abs(x_2 - x_1) == 1)):
#     print("YES")
# else:
#     print("NO")
# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print("Равносторонний")
# elif a == b != c or b == c != a or a == c != b:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")


# a = int(input())
# b = int(input())
# m = max(a, b)
# print(m)


# a_1, b_1, a_2, b_2 = int(input()), int(input()), int(input()), int(input())
# max_a = max(a_1, a_2)
# max_b = max(b_1, b_2)
# min_a = min(a_1, a_2)
# min_b = min(b_1, b_2)
# if max_a > min_b and min_a < max_b:
#     print("пустое множество")
# elif min_b == max_a and max_b > min_a:
#     print(max_a)
# elif max_a < min_b and min_a < max_b:
#     print(max_a, min_b)
# elif max_a == min_a
#     print(min_a, min_b)
# elif max_b == min_b:
#     print(max_a, max_b)
# elif max_a == min_a and max_b == min_b:
#     print(a_1, b_1)


# n = int(input())
# if 0 < n < 11:
#     if n < 4:
#         print(n * "I")
#     elif n == 4:
#         print("IV")
#     elif n < 9:
#         print("V" + (n-5) * "I")
#     elif n < 11:
#         print((10 - n) * "I" + "X")
# else:
#     print("ошибка")


# a, b, c = int(input()), int(input()), int(input())
# s = 0
# if c >= a >= b or b >= a >= c:
#     s += a
# elif a >= c >= b or b >= c >= a:
#     s += c
# else:
#     s += b
# print(max(a, b, c))
# print(s)
# print(min(a, b, c))


# a, b, c = input(), input(), input()
#
# if(len(a) < len(b)): b, a = a, b
# if(len(c) > len(b)): c, b = b, c
# if(len(c) > len(a)): c, a = a, c
#
# print(c, a, sep='\n')


# from math import *
# n, a = float(input()), float(input())
# print((n * a ** 2) / (4 * tan(pi/n)))

# from math import *

# n = int(input())
# print("1", end=" ")
# total_1, total_2 = 1, 0
# for i in range(1, n + 1):
#     if n != 1:
#         total_1, total_2 = total_2 + total_1, total_1
#         print(total_1, end=" ")


# n = int(input())
# flag = True
# cmp = 0
# while n > 9:
#     a = n % 10
#     comp = n // 10 % 10
#     if a > comp:
#         flag = False
#     print(a, comp)
#     n = n // 10
# if flag:
#     print("YES")
# else:
#     print("NO")


# n = int(input())
# h = n // 2 + 1
# for j in range(1, h + 1):
#     print(j * '*')
# for i in range(h - 1, 0, -1):
#     print(i * '*')


# for i in range(1, 14):
#     for k in range(1, 13):
#         for j in range(1, 12):
#             if 28 * i + 30 * k + 31 * j == 365:
#                 print(i, k, j)


# for i in range(1, 11):
#     for j in range(1, 21):
#         for k in range(1, 200):
#             if 10 * i + 5 * j + 0.5 * k == 100 and i + j + k == 100:
#                 print(i, j, k)


# for a in range(1, 50):
#     for b in range(1, 50):
#         for c in range(1, 50):
#             for d in range(1, 50):
#                 for e in range(1, 50):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                         print(a + b + c + d + e)


# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         total += 1
#         print(total, end=" ")
#     print()


# s = input()
# counter_1, counter_2 = 0, 0
# for i in range(len(s)):
#     if s[i].lowe() in ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]:
#         counter_1 += 1
#     if s[i].lower() in ["б", "в", "г", 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш','щ']:
#         counter_2 += 1
# print(f"Количество гласных букв равно {counter_1}")
# print(f"Количество согласных букв равно {counter_2}")


# s = 'abcdef'
#
# print(s[len(s) // 2 + len(s) % 2:], s[:len(s) // 2 + len(s) % 2], sep='')


# n = int(input())
# s = input()
# for c in s:
#     a = ord(c) - n
#     if a < 97:
#         a = 122 - (96 - a)
#     print(chr(a), end='')


# l = list()
# for i in range(1, 27):
#     l.append(chr(96 + i) * i)
# print(l)
# print(len(l[-1]))


# n = int(input())
# l = list()
# for _ in range(n):
#     s = input()
#     l.append(s)
# k = input()
# for i in l:
#     if k.lower() in i.lower():
#         for c in i.strip():
#             print(c, end='')
#         print()

# l1 = list()
# l2 = list()
# l3 = list()
# n = int(input())
# for _ in range(n):
#     l1.append(input())
# k = int(input())
# for _ in range(k):
#     l2.append(input())
# for i in l1:
#     counter = 0
#     for j in l2:
#         if j.lower() in i.lower():
#             counter += 1
#     if counter == len(l2):
#         l3.append(i)
# for i in l3:
#     print(i)


# l = list(input().split('\\'))
# print(*l, sep='\n')


# l = list()
# s = input()
# l.append(s)
# print(*l)


# l = list(input().split())
# total = 0
# for i in range(len(l)):
#     counter = 0
#     for j in range(len(l) - 1, i, -1):
#         if l[i] == l[j]:
#             counter += 1
#     total += counter
# print(total)


# n = [8, 9, 10, 11]
# n[1] = 17
# s = 456
# n.extend([4, 5, 6])
# del n[0]
# n *= 2
# n.insert(3, 25)
# print(n)


# l = input().split()
# for i in range(len(l)):
#     l[i] = int(l[i])
# a = max(l)
# b = min(l)
# i = l.index(a)
# j = l.index(b)
# l[i] = b
# l[j] = a
# print(*l)


# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
#      -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71,
#      -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
#      -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
#
# n = len(a)
# l = list()
# # реализация алгоритма сортировки выбором
# for i in range(n):
#     l.append(min(a))
#     a.remove(min(a))
#
# print(l)

# # объявление функции
# def draw_box():
#     print("*" * 10)
#     for _ in range(12):
#         print("*", "*", sep='' * 8)
#     print("*" * 10)
# # основная программа
# draw_box()  # вызов функции


# # объявление функции
# def get_days(month):
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif month == 2:
#         return 28
#     else:
#         return 30
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(get_days(num))


# # объявление функции
# def find_all(target, symbol):
#     a = list()
#     l = [c for c in target]
#     counter = 0
#     while symbol in l:
#         a.append(l.index(symbol) + counter)
#         l.remove(symbol)
#         counter += 1
#     return a
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))


# # объявление функции
# def is_palindrome(text):
#     result = True
#     l = [i.lower() for i in text if i.isalpha()]
#
#     if l[:] != l[::-1]:
#         result = False
#     return result, l
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))


# # Prime number
# def is_prime(num):
#     flag = False
#     for i in range(2, num):
#         if num % i == 0:
#             flag = True
#     if num == 1:
#         return False
#     if flag:
#         return False
#     else:
#         return True
#


# # объявление функции
# def is_correct_bracket(text):
#     result = True
#     counter = 0
#     list_empty = []
#     list = [i for i in text]
#     limit = 0
#
#     if list[0] == ')' or list[-1] == '(':
#         result = False
#
#     a, b = list.count('('), list.count(')')
#     if a != b or a > b or b > a:
#         result = False
#
#
#     while limit < 100:
#         for i in range(len(list) - 1):
#             if list[i] == '(' and list[i + 1] == ')':
#                 del list[i]
#                 del list[i]
#                 break
#         limit += 1
#     if len(list) != 0:
#         result = False
#
#     return result
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))

# def solve(a, b, c):
#     d = ((b ** 2) - 4 * a * c) ** 0.5
#     return min((-b - d) / (2 * a), (-b + d) / (2 * a)), max((-b - d) / (2 * a), (-b + d) / (2 * a))
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2, sep=' ')


# # объявление функции
# def is_pangram(text):
#     counter = 0
#     l = sorted(set(text.lower().replace(' ', '')))
#     for c in l:
#         if c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
#             counter += 1
#     if counter == 26:
#         return True
#     else:
#         return False
#
# # считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))

print("Хотите еще раз?\nYes - Y\nNo - N")
