import asyncio


async def activate_portal(x):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 2


async def teleportation(x):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 2


async def charge(x):
    print(f'Подзарядка портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 3


async def stability(x):
    print(f'Проверка стабильности портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 4


async def recovery(x):
    print(f'Восстановление портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 5


async def close(x):
    print(f'Закрытие портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x - 1


async def portal_operator():
    answers = [
        'Результат активации портала: {} единиц энергии',
        'Результат телепортации: {} единиц времени',
        'Результат подзарядки портала: {} единиц энергии',
        'Результат проверки стабильности: {} единиц времени',
        'Результат восстановления портала: {} единиц энергии',
        'Результат закрытия портала: {} единиц времени'
    ]
    tasks = {'activation': await asyncio.create_task(activate_portal(2)),
             'teleportation': await asyncio.create_task(teleportation(3))}
    recharge, check, recover = await asyncio.gather(
        *[asyncio.create_task(charge(4)), asyncio.create_task(stability(5)), asyncio.create_task(recovery(6))])
    tasks['recharge'] = recharge
    tasks['check'] = check
    tasks['recover'] = recover
    closed = await asyncio.create_task(close(7))
    tasks['closed'] = closed
    print(*[text.format(value) for text, value in zip(answers, tasks.values())], sep='\n')


if __name__ == '__main__':
    asyncio.run(portal_operator())
