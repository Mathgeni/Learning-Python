import asyncio


async def my_coroutine():
    print('start')
    await asyncio.sleep(2)
    print('End')


async def main():
    await asyncio.create_task(my_coroutine())


if __name__ == '__main__':
    asyncio.run(main())
