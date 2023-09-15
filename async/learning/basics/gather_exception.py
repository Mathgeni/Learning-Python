import asyncio


async def cor():
    raise Exception


async def main():
    res = await asyncio.gather(cor(), return_exceptions=True)
    print(res)

if __name__ == '__main__':
    asyncio.run(main())
