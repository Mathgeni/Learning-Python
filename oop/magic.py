class Word(str):
    '''Класс для слов, определяющий сравнение по длине слов.'''

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')]  # Теперь Word это все символы до первого пробела
        return str.__new__(cls, word)


x = Word('asd f')
print(x)

print(x.__eq__('asdf'))
