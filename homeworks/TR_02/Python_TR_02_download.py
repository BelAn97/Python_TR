#     Создать скрипт, который параллельно скачает содержимое нескольких сайтов и сохранит их содержимое на диск.

import asyncio
import os
from os.path import dirname, abspath, join

import aiohttp as aiohttp


def save_to_disk(url, text):
    path = join(dirname(abspath(__file__)), "sites")
    os.makedirs(path, exist_ok=True)
    with open(join(path, url.split('//')[1]+'.txt'), 'w', encoding='utf-8') as f:
        f.write(text)


async def download_sites(*args):
    async with aiohttp.ClientSession() as session:
        for url in args:
            async with session.get(url) as response:
                save_to_disk(url, await response.text())


asyncio.run(download_sites('https://ya.ru', 'https://www.google.ru'))
