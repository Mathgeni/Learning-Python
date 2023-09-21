import asyncio


async def camera(id, ip, event):
    print(f'Датчик {id} IP-адрес {ip} настроен и ожидает срабатывания')
    await event.wait()
    print(f'Датчик {id} IP-адрес {ip} активирован, "Wee-wee-wee-wee"')


async def move(event):
    await asyncio.sleep(2)
    print('Датчики зафиксировали движение')
    event.set()


async def main():
    alarm = asyncio.Event()
    ips = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]
    tasks = [asyncio.create_task(camera(_id, ip, alarm)) for _id, ip in enumerate(ips)]
    await asyncio.gather(*tasks, asyncio.create_task(move(alarm)))


if __name__ == '__main__':
    asyncio.run(main())
