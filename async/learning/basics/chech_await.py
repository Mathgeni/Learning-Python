import asyncio
import time

# Проверка на конкуренсть выполнения

async def count(n: int):
    print(n)
    await asyncio.sleep(n)
    print(n)


async def main():
    tasks = [asyncio.create_task(count(n)) for n in range(5)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
