with open('prices.txt', encoding='utf-8') as file:
    print('Repeat oop me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')