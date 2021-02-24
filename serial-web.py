import requests

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

for url in urls:
    res = requests.get(url)
    print(res.text[:100])