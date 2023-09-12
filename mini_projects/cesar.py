alpha_en = [chr(i) for i in range(97, 123)]
alpha_ru = [chr(i) for i in range(1072, 1104)]
alpha_En = [chr(i) for i in range(65, 91)]
alpha_Ru = [chr(i) for i in range(1040, 1072)]

def encryption_ru(s, n):
    list_in = [i for i in s]
    list_out = []
    for c in list_in:
        if c in alpha_ru:
            list_out.append(alpha_ru[(alpha_ru.index(c) + n) % 32])
        elif c in alpha_Ru:
            list_out.append(alpha_Ru[(alpha_Ru.index(c) + n) % 32])
        elif c == ' ':
            list_out.append(' ')
        else:
            list_out.append(c)
    return list_out

def decryption_ru(s, n):
    list_in = [i for i in s]
    list_out = []
    for c in list_in:
        if c in alpha_ru:
            list_out.append(alpha_ru[(alpha_ru.index(c) - n) % 32])
        elif c in alpha_Ru:
            list_out.append(alpha_Ru[(alpha_Ru.index(c) - n) % 32])
        elif c == ' ':
            list_out.append(' ')
        else:
            list_out.append(c)
    return list_out

def encryption_en(s, n):
    list_in = [i for i in s]
    list_out = []
    for c in list_in:
        if c in alpha_en:
            list_out.append(alpha_en[(alpha_en.index(c) + n) % 26])
        elif c in alpha_En:
            list_out.append(alpha_En[(alpha_En.index(c) + n) % 26])
        elif c == ' ':
            list_out.append(' ')
        else:
            list_out.append(c)
    return list_out

def decryption_en(s, n):
    list_in = [i for i in s]
    list_out = []
    for c in list_in:
        if c in alpha_en:
            list_out.append(alpha_en[(alpha_en.index(c) - n) % 26])
        elif c in alpha_En:
            list_out.append(alpha_En[(alpha_En.index(c) - n) % 26])
        elif c == ' ':
            list_out.append(' ')
        else:
            list_out.append(c)
    return list_out

while True:
    print("Выберите направление:\nДешифрование - д\nШифрование - ш")
    choice = input()
    print('Язык:')
    language = input()
    print('Введите текст:')
    s = input()
    print("Введите шаг:")
    n = int(input())
    out = []
    if language.lower() == 'ру':
        if choice == 'ш':
            out = encryption_ru(s, n)
            for c in out:
                print(c, end='')
            print()
        elif choice == 'д':
            out = decryption_ru(s, n)
            for c in out:
                print(c, end='')
            print()
        else:
            print('Введите д или ш')
            print()
    elif language.lower() == 'ин':
        if choice == 'ш':
            out = encryption_en(s, n)
            for c in out:
                print(c, end='')
            print()
        elif choice == 'д':
            out = decryption_en(s, n)
            for c in out:
                print(c, end='')
            print()
        else:
            print('Введите д или ш')
            print()