#!/usr/bin/python3

#corroutines using asyncio
import asyncio


#Coroutine function
async def greet(name):
    return (f"Hola {name}")


#coroutines can be launched through othere couroutines
async def main():
    greeting = await greet("Enrique")
    print(greeting)

if __name__== "__main__":
    asyncio.run(main())
