#!/usr/bin/python3

# corroutines using asyncio
import asyncio


# Coroutine function
async def cancellable_task():
    try:
        while True:
            print("hola, task is running")
            await asyncio.sleep(0.5)
    except asyncio.CancelledError:
        print("Task ha been cancelled")
    finally:
        print("Pelaste")


# coroutines can be launched through othere couroutines
async def main():
    task = asyncio.create_task(cancellable_task())
    print(f"Context:{task.get_context()}")
    await asyncio.sleep(2)
    task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
