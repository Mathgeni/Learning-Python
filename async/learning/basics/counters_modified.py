import asyncio


# Конкурентный вывод счетчиков и исполнение

async def coroutine(max_count: dict[str, int], counters: dict[str, int], name: str, delay: int) -> None:
    while counters[name] < max_count[name]:
        counters[name] += 1
        await asyncio.sleep(delay)
        print(f'{name}: {counters[name]}')


async def main():
    max_counts = {
        "Counter 1": 10,
        "Counter 2": 5,
        "Counter 3": 15,
    }
    delays = {
        "Counter 1": 1,
        "Counter 2": 2,
        "Counter 3": 0.5,
    }
    counters = {
        "Counter 1": 0,
        "Counter 2": 0,
        "Counter 3": 0,
    }
    tasks = [asyncio.create_task(coroutine(max_counts, counters, name, delays[name])) for name in
             ['Counter 1', 'Counter 2', 'Counter 3']]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
