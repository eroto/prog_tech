#!/usr/bin/python3

import asyncio
from utils.dist_queue import AsyncScrapper


async def main():
    urls = [
        "https://httpbin.org/uuid",
        "https://httpbin.org/uuid",
        "https://httpbin.org/uuid"
        #"https://api.github.com/events"
    ]

    scrapper = AsyncScrapper(urls)

    ret = await(scrapper.run())
    print(f"ret: {ret}")


if __name__== "__main__":
    asyncio.run(main())
    print("Concurrency...")