# ideas from here: https://stackoverflow.com/questions/22190403/how-could-i-use-requests-in-asyncio
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter00-introduction/',
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter01-getting-started/',
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter02-cloud-foundations/',
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter03-virtualization-containers-elasticity',
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter04-distributed-computing',
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter05-cloud-storage',
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter06-serverless-etl',
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter07-managed-ml',
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter08-data-science-case-studies',
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter09-essays',
                'https://paiml.com/docs/home/books/cloud-computing-for-data/chapter10-career'
            ]

    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        htmls = await asyncio.gather(*tasks)
        for html in htmls:
            print(html[:100])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())