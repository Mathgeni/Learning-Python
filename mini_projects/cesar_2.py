alpha_En = [chr(i) for i in range(65, 91)]
alpha_en = [chr(i) for i in range(97, 123)]

s = input()
l_in = [i for i in s.split()]
l_out = []
for s in l_in:
    counter = 0
    for c in s:
        if c in alpha_en or c in alpha_En:
            counter += 1
    for c in s:
        if c in alpha_en:
            l_out.append(alpha_en[(alpha_en.index(c) + counter) % 26])
        elif c in alpha_En:
            l_out.append(alpha_En[(alpha_En.index(c) + counter) % 26])
        else:
            l_out.append(c)
    l_out.append(' ')
for c in l_out:
    print(c, end='')