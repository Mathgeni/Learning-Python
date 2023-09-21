import asyncio


async def producer(queue):
    for i in range(10):
        try:
            print(i)
            queue.put_nowait(i)
        except asyncio.QueueFull:
            pass


async def consumer(queue):
    while True:
        try:
            task = queue.get_nowait()
            print(f'{task}')
            queue.task_done()
        except asyncio.QueueEmpty:
            break


async def main():
    queue = asyncio.LifoQueue()
    task = await asyncio.create_task(producer(queue))
    task = await asyncio.create_task(consumer(queue))


if __name__ == '__main__':
    asyncio.run(main())
