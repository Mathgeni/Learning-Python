import asyncio


async def coroutine(a):
    b = a + 3
    return b


async def main():
    task = asyncio.create_task(coroutine(3))
    print(task.print_stack())


if __name__ == '__main__':
    asyncio.run(main())
