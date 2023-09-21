import asyncio

### asyncio.CancelledError must have excepted in try/except block


async def cor():
    return 'Hello'


async def main():
    task = asyncio.create_task(cor())
    task.cancel()
    try:
        response = await task
        print(response)

    except asyncio.CancelledError:
        print('Cancelled')


if __name__ == '__main__':
    asyncio.run(main())
