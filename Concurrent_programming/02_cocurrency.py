#!/usr/bin/python3

#corroutines using asyncio
import asyncio


#Coroutine function
async def count():
    print("one")
    await asyncio.sleep(1)
    print("two")

#Coroutine function
async def sum():
    print(6+5)
    await asyncio.sleep(1)
    print("adios")


#main coroutines to launch a couroutine
async def main():
    await asyncio.gather(count(), sum())

if __name__== "__main__":
    asyncio.run(main())