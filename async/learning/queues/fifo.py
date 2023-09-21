import asyncio
import random


async def worker(queue, name):
    while True:
        task = await queue.get()    # take task
        print(f'Worker {name} got coroutine {task}')
        await asyncio.sleep(2)
        queue.task_done()           # task done


async def main():
    queue = asyncio.Queue()
    for _ in range(10):
        await queue.put(random.randint(1, 10))
    tasks = [asyncio.create_task(worker(queue, f'{i}')) for i in range(3)]
    await queue.join()      # Waits for all workers are done
    for task in tasks:
        task.cancel()


if __name__ == '__main__':
    asyncio.run(main())
