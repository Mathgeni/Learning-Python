import random


with open('first_names.txt', 'r', encoding='utf-8') as f, open('last_names.txt', 'r', encoding='utf-8') as l:
    z, x = f.readlines(), l.readlines()
    for i in range(3):
        print(random.choice(z).strip(), random.choice(x).strip(), sep=' ')