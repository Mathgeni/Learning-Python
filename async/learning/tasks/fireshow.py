import asyncio
import itertools
import random


async def fire(color, shape, action):
    print(f'Запущен {color} {shape} салют, в форме {action}!!!')
    await asyncio.sleep(random.randint(1, 5))
    print(f'Салют {color} {shape} завершил выступление {action}')


async def main():
    shapes = ["circle", "star", "square", "diamond", "heart"]
    colors = ["red", "blue", "green", "yellow", "purple"]
    actions = ["change_color", "explode", "disappear"]

    combinaitons = list(itertools.product(shapes, colors, actions))
    tasks = [asyncio.create_task(fire(color, shape, action)) for shape, color, action in combinaitons]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())