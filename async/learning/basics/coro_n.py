import asyncio


async def coro(n):
    await asyncio.sleep(1)
    print(f'Coroutine {n} is done')


async def main():
    [await asyncio.create_task(coro(i)) for i in range(10)]


asyncio.run(main())
