import asyncio


# Моделирование прерывания

async def polling():
    while True:
        print('Polling')
        await asyncio.sleep(1)


async def interruption(flag):
    while True:
        await asyncio.sleep(3)
        if flag.is_set():
            print('Interruption')
            flag.clear()
            break
    return flag


async def main():
    flag = asyncio.Event()
    task1 = asyncio.create_task(polling())
    task2 = asyncio.create_task(interruption(flag))
    while True:
        await asyncio.sleep(2)
        flag.set()
        flag = await task2
        task2 = asyncio.create_task(interruption(flag))


if __name__ == '__main__':
    asyncio.run(main())
