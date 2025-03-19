from time import sleep
import asyncio


async def mul(a, b):
    #print(f"multipliying {a}*{b}")
    #sleep(2)
    await asyncio.sleep(2)
    return a * b


async def sum(a, b):
    #print(f"adding {a}+{b}")
    #sleep(3)
    await asyncio.sleep(3)
    return a + b


async def saluda(nombre):
    #print(f"Hola {nombre}")
    #sleep(3)
    await asyncio.sleep(3)
    #print(f"Adios {nombre}")
    return 1


async def printer(symbol):
    for i in range(100):
        print(f"{symbol}", end="")
        #sleep(0.01)
        await asyncio.sleep(0.01)
    print(f"|")
    return 1


if __name__ == "__main__":
    saluda("Paula")
    sum(23, 45)
