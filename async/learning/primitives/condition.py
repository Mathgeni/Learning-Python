import asyncio

TOTAL_CONNECTIONS = 0


async def request(name, condition):
    global TOTAL_CONNECTIONS
    async with condition:
        print(f'Пользователь {name} ожидает доступа к базе данных')
        await condition.wait()
        print(f'Пользователь {name} подключился к БД')
        TOTAL_CONNECTIONS += 1
        await asyncio.sleep(0.5)
        print(f'Пользователь {name} отключается от БД')
        print(TOTAL_CONNECTIONS)
        condition.notify()


async def connection(condition):
    async with condition:
        condition.notify(1)


async def main():
    condition = asyncio.Condition()
    users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']
    tasks = [asyncio.create_task(request(name, condition)) for name in users]
    await asyncio.gather(*tasks, connection(condition))


if __name__ == '__main__':
    asyncio.run(main())
