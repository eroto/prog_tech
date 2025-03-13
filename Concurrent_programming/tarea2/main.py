#!/usr/bin/python3

import asyncio
import multiprocessing as mp
from utils.dist_queue import AsyncScrapper

def foo(q):
    q.put('hello')

async def the_task(q):
    #await(num)
    q.put(5*5)


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

    mp.set_start_method('spawn')
    q = mp.Queue(2)
    p1 = mp.Process(target=foo, args=(q,))
    p2 = mp.Process(target=the_task, args=(q,))
    p1.start()
    p2.start()
    print(f"q.get():{q.get()}")
    p1.join()
    p2.join()