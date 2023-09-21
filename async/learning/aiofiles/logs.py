import asyncio
import glob
import re
import aiofiles

file_dir = '/home/mathgeni/Downloads/chat_log/'


async def logger(file):
    out = list()
    async with aiofiles.open(file) as f:
        lines = await f.readlines()
        for line in lines:
            customer, words = re.findall(r'\s([\w, \s]+): ([\w, \s]+.)', line)[0]
            out.append((customer, words))
    return out


async def main():
    customers = dict()
    tasks = [asyncio.create_task(logger(file)) for file in glob.glob(f'{file_dir}*.txt')]
    result = await asyncio.gather(*tasks)
    for messages in result:
        for customer, message in messages:
            customers[customer] = customers.get(customer, 0.0) + float(len(message)) * 0.03
    out = {key: f"{round(value, 2)}р" for key, value in
           sorted(customers.items(), key=lambda customer: customer[1], reverse=True)}
    print(out)


if __name__ == '__main__':
    asyncio.run(main())
