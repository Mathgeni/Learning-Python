import asyncio

# Атомарность

total = 0
lock = asyncio.Lock()


async def change():
    global total
    async with lock:
        total += 1
        await asyncio.sleep(1)
    print(total)


async def main():
    await asyncio.gather(*[change() for _ in range(5)])


if __name__ == '__main__':
    asyncio.run(main())
