#!/usr/bin/python3

# execute several corroutines concurrently

import asyncio


# Coroutine function
async def sim_io(numero):
    print(f"Inicio {numero}")
    # simular un request IO
    await asyncio.sleep(numero)
    print(f"Fin de {numero}")
    return f"Resultado de numero {numero}"


# coroutines can be launched through othere couroutines
async def main():
    coroutine1 = sim_io(3)
    coroutine2 = sim_io(5)
    coroutine3 = sim_io(1)
    resultados = await asyncio.gather(coroutine1, coroutine2, coroutine3)
    
    for resultado in resultados:
        print(resultado)


if __name__ == "__main__":
    asyncio.run(main())

    
