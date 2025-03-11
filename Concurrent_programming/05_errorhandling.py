#!/usr/bin/python3

#corroutines using asyncio
import asyncio


#Coroutine function
async def faulty_coroutine():
    print(f"hola")
    await asyncio.sleep(1) #simular IO
    raise ValueError("Croutine failed!!")


#coroutines can be launched through othere couroutines
async def main():
    try:
        await faulty_coroutine()
    except ValueError as e:
        print(f"Catch exception {e}")

if __name__== "__main__":
    asyncio.run(main())