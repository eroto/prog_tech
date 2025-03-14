#!/usr/bin/python3

#corroutines using asyncio
import asyncio


#Coroutine function
async def my_coroutine():
    print(f"MyCorroutine")
    await asyncio.sleep(1)
    return(f"result {3*2}") #this is known as a future

#Coroutine function
async def sum():
    print(6+5)
    await asyncio.sleep(1)
    print("adios")


#main coroutines to launch a couroutine
async def main():
    task = asyncio.create_task(my_coroutine())
    print(type(task))
    #si no se ha completado la ejecucion 
    #espera a que me regrese el valor
    result = await task
    print(f"result:{result}")

if __name__== "__main__":
    asyncio.run(main())