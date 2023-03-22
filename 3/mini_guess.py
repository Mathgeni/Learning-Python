from random import *

def is_valid(a):
    result = True
    if a > 100 or a < 1:
        result = False
    return result

choice = "Y"

print('\nДобро пожаловать в числовую угадайку\n')

while choice.lower() == "y":

    print("Выберите правую границу:\n")
    border = int(input())
    number = randrange(1, border + 1)
    comparator = True
    counter = 0

    print("\nВведите число:\n")

    while comparator:

        counter += 1
        attempt = int(input())

        if is_valid(attempt):
            if attempt < number:
                print("\nСлишком мало, попробуйте еще раз\n")

            elif attempt > number:
                print("\nСлишком много, попробуйте еще раз\n")

            else:
                print("\nВы угадали, поздравляем!")
                print(f"Число попыток: {counter}\n")
                comparator = False
        else:
            print('\nА может быть все-таки введем целое число от 1 до 100?\n')
    print("...")
    print("Хотите еще раз?\nYes - Y\nNo - N\n")
    choice = input()

print("\nСпасибо, что играли в числовую угадайку. Еще увидимся...")