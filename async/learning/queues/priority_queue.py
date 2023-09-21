import asyncio
import random


async def getter(queue):
    priority, task = await queue.get()
    return priority, task


async def putter(queue, priority, data):
    await queue.put((priority, data))       # tuple


async def main():
    queue = asyncio.PriorityQueue()
    tasks = [asyncio.create_task(putter(queue, random.randint(1, 3), i)) for i in range(10)]
    await asyncio.gather(*tasks)
    while not queue.empty():
        priority, task = await getter(queue)
        print(f'Data:{task} Priority: {priority}')


if __name__ == '__main__':
    asyncio.run(main())
