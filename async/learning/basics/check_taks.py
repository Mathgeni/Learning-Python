import asyncio


# Таски сразу же грузятся в стек без явного вызова

async def task(n):
    print(f'task: {n}')


async def main():
    task1 = asyncio.create_task(task(1))
    await asyncio.sleep(2)
    task1 = asyncio.create_task(task(2))
    await asyncio.sleep(2)


if __name__ == '__main__':
    asyncio.run(main())
