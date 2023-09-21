import asyncio
import glob

import aiofiles

file_path = '/home/mathgeni/Downloads/files/files/'
total = 0


async def counter(file):
    global total
    async with aiofiles.open(file, mode='r') as file:
        number = await file.read()
        total += int(number) if int(number) % 2 == 0 else 0


async def main():
    tasks = [asyncio.create_task(counter(file)) for file in glob.glob(f'{file_path}*.txt')]
    await asyncio.gather(*tasks)
    print(total)


if __name__ == '__main__':
    asyncio.run(main())
