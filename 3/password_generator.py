from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuations = '!#$%&*+-=?@^_.'
chars = ''

print('Количество паролей для генерации:')
n = int(input())
print('Длина пароля:')
l = int(input())
print('Включать ли цифры 0123456789?')
answer_d = input()
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
answer_u = input()
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
answer_l = input()
print('Включать ли символы !#$%&*+-=?@^_?')
answer_p = input()
print("Исключать ли неоднозначные символы il1Lo0O?")
answer_del = input()

if answer_d.lower() == 'да':
    chars = chars + digits
if answer_u.lower() == 'да':
    chars = chars + uppercase_letters
if answer_l.lower() == 'да':
    chars = chars + lowercase_letters
if answer_p.lower() == 'да':
    chars = chars + punctuations
if answer_del.lower() == 'да':
    for c in "il1Lo0O":
        chars = chars.replace(c, '')
def generate_password(s, lenth):
    list = []
    for _ in range(n):
        sublist = []
        for i in range(lenth):
            sublist.append(choice(s))
        list.append(sublist)
    return list

passwords = generate_password(chars, l)

for s in passwords:
    for c in s:
        print(c, end='')
    print()

