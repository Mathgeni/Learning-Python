import asyncio


# Одновременный вывод счетчиков

async def coro(current_values, name, delay):
    current_values[name] += 1
    await asyncio.sleep(delay)
    return name


async def comparison(max_values, current_values):
    for key in max_values.keys():
        if max_values[key] != current_values[key]:
            return False
    return True


async def index(max_values, current_values, name):
    return max_values[name] == current_values[name]


async def main():
    max_values = {
        "Counter 1": 10,
        "Counter 2": 5,
        "Counter 3": 15
    }
    current_values = {
        "Counter 1": 0,
        "Counter 2": 0,
        'Counter 3': 0
    }

    while not await comparison(max_values, current_values):
        tasks = [asyncio.create_task(coro(current_values, name, 1)) for name in ['Counter 1', 'Counter 2']
                 if not await index(max_values, current_values, name)]
        res = await asyncio.gather(*tasks)
        for key, value in current_values.items():
            if key in res:
                print(f'{key}: {value}')


asyncio.run(main())
