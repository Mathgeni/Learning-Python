import asyncio


async def activate_portal(x: int) -> int:
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x: int) -> int:
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 2


async def portal_operator():
    activation = await asyncio.create_task(activate_portal(2))
    if activation > 4:
        teleportation = await asyncio.create_task(perform_teleportation(1))
    else:
        teleportation = await asyncio.create_task(perform_teleportation(activation))
    print(f'Результат активации портала: {activation} единиц энергии')
    print(f'Результат телепортации: {teleportation} единиц времени')


if __name__ == '__main__':
    asyncio.run(portal_operator())
