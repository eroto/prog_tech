#!/usr/bin/python3

import asyncio

from utils.scrapper import AsyncScrapper


urls = [
        "http://httpbin.org/uuid",
        "https://api.github.com/events",
        "http://google.com",
    ]

async def main():

    scrapper = AsyncScrapper(urls)

    await scrapper.run()


if __name__ == "__main__":
    asyncio.run(main())
