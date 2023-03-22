import random
import string

alp = list(string.digits + string.ascii_lowercase + string.ascii_uppercase)
alp = list(filter(lambda x: x not in 'lI1oO0', alp))


def password(n, m):
    return [[random.choice(alp) for _ in range(m)] for _ in range(n)]


n = int(input())
m = int(input())

for i in password(n, m):
    print(*i, sep='')

