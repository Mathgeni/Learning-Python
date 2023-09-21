import asyncio


async def coro(n):
    await asyncio.sleep(2)
    return n


async def main():
    task = asyncio.create_task(coro(2))
    try:
        await asyncio.wait_for(task, timeout=3)
        print(task.result())

    except asyncio.TimeoutError:
        print('Exit')

if __name__ == '__main__':
    asyncio.run(main())