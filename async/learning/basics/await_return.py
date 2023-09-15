import asyncio
import time


# Проверка как работает return

async def add_one(n):
    await asyncio.sleep(n)
    return n + 1


async def main():
    res = await asyncio.gather(*[add_one(n) for n in range(1, 6)])
    print(res)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
