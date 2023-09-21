import asyncio

TOTAL_CONNECTIONS = 0


async def connection(name, semaphore):
    global TOTAL_CONNECTIONS
    async with semaphore:
        print(f'Пользователь {name} делает запрос')
        TOTAL_CONNECTIONS += 1
        await asyncio.sleep(1)
        print(f'Запрос от пользователя {name} завершен')
        print(f'Всего запросов: {TOTAL_CONNECTIONS}')


async def main():
    users = ["sasha", "petya", "masha", "katya", "dima", "olya", "igor", "sveta", "nikita", "lena",
             "vova", "yana", "kolya", "anya", "roma", "nastya", "artem", "vera", "misha", "liza"]
    semaphore = asyncio.Semaphore(3)
    tasks = [asyncio.create_task(connection(name, semaphore)) for name in users]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
