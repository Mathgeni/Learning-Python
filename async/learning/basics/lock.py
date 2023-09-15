import asyncio

# Лок


async def info(iterable, item, lock):
    async with lock:
        iterable.append(item)
    print(iterable)


async def main():
    lock = asyncio.Lock()
    total = []
    await asyncio.gather(*[info(total, i, lock) for i in range(10)])

if __name__ == '__main__':
    asyncio.run(main())
