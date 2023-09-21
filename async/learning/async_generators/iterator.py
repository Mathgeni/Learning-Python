import asyncio
import random


class AsyncUrl:
    def __init__(self, urls, start=0):
        self.urls = urls
        self.start = start

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.start >= len(self.urls):
            raise StopAsyncIteration
        self.start += 1
        return self.urls[self.start - 1]


async def main():
    urls = AsyncUrl(['https://google.com', 'https://yandex.ru', 'https://4123', 'https://fdsasafd'])
    res = [url async for url in urls]
    print(res)


if __name__ == '__main__':
    asyncio.run(main())
