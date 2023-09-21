import asyncio

enters = 0


async def robot(name, id, lock):
    global enters
    async with lock:
        print(f'Робот {name}({id}) передвигается к месту A')
        enters += 1
    print(f'Робот {name}({id}) достиг места A. Место A посещено {enters} раз')


async def main():
    lock = asyncio.Lock()
    robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']
    tasks = [asyncio.create_task(robot(robot_names[i], i, lock)) for i in range(5)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
