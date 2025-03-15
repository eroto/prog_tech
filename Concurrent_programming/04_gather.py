#!/usr/bin/python3

# corroutines using asyncio
import asyncio


# Coroutine function
async def worker(number):
    print(f"Worfer {number} started")
    await asyncio.sleep(2)  # simular IO
    print(f"Worker {number} finished")
    return f"result from worker {1}"


# Coroutine function
async def worker2(number):
    print(f"Worfer {number} started")
    await asyncio.sleep(2)  # simular IO
    while True:
        print("hola")
    print(f"Worker {number} finished")
    return f"result from worker {1}"


# coroutines can be launched through othere couroutines
async def main():
    results = await asyncio.gather(worker(1), worker(2), worker(3), worker2(4))
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
