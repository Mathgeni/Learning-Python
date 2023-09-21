import asyncio


async def coro(d):
    print(asyncio.current_task().get_name())
    await asyncio.sleep(d)
    print(asyncio.current_task().get_name())


async def main():
    tasks = [asyncio.create_task(coro(x)) for x in range(10)]
    done, pending = await asyncio.wait(tasks, timeout=5)


if __name__ == '__main__':
    asyncio.run(main())
