import asyncio


async def translate(index):
    codes = ["56FF4D", "A3D2F7", "B1C948", "F56A1D", "D4E6F1",
             "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
             "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]
    return codes[index]


async def message(text, index):
    code = await translate(index)
    try:
        print(f'Сообщение: {text}' if int(code[-1]) % 2 != 0 else 'Сообщение: Неверный код, сообщение скрыто')
        print(f'Код: {code}')
    except ValueError:
        print(f'Сообщение: {text}', f'Код: {code}', sep='\n')


async def main():
    messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
                "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
                "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!",
                "Всего наилучшего!"]
    await asyncio.gather(*[asyncio.create_task(message(text, i)) for i, text in enumerate(messages)])


if __name__ == '__main__':
    asyncio.run(main())
