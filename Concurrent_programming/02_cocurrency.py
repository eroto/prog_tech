#!/usr/bin/python3

# corroutines using asyncio
import asyncio


# Coroutine function
async def count():
    print("one")
    await asyncio.sleep(0.5)
    print("two")


# Coroutine function
async def sum():
    print("Calculando 6+5")
    resultado = 6 + 5
    await asyncio.sleep(3)
    print(f"resultado:{resultado}")


async def saluda(nombre):
    print(f"Hola {nombre}")
    await asyncio.sleep(3)
    print(f"Adios {nombre}")


async def printer():
    for i in range(100):
        print("=.", end="")
        await asyncio.sleep(0.01)

    # for i in range(100):
    #    print(".=.", end="")


# main coroutines to launch a couroutine
async def main():
    # Gather takes
    print("Startinggather")
    await asyncio.gather(count(), printer(), sum(), saluda("Pepe"))


if __name__ == "__main__":
    asyncio.run(main())
