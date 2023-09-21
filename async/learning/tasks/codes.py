import asyncio


def translate(task):
    codes = ["56FF4D", "A3D2F7", "B1C94E", "F56A1D", "D4E6F1",
             "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
             "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F0"]
    index = task.result()
    print(f'Код: {codes[index]}')


async def message(index, text):
    print(f'Сообщение: {text}')
    asyncio.current_task().add_done_callback(translate)
    return index


async def main():
    messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
                "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
                "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!",
                "Всего наилучшего!"]

    for i, text in enumerate(messages):
        task = await asyncio.create_task(message(i, text))


if __name__ == '__main__':
    asyncio.run(main())
