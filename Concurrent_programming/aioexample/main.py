#!/usr/bin/python3

import asyncio
from utils.scrapper import AsyncScrapper


async def main():
    urls = [
        "http://httpbin.org/uuid",
        "https://api.github.com/events",
        "http://httpbin.org/uuid",
    ]

    scrapper = AsyncScrapper(urls)

    scrapper.run()


if __name__== "__main__":
    asyncio.run(main())