#!/usr/bin/python3
from functools import reduce
import time


def decorator(func): #decorador, recive una funcion
    def envoltura(): #Genera el codigo nuevo que quiero agregar a la funcion oirigal
        print("Inside decorartor before calling the function")
        start = time.time()
        func() #Aqui se ejecuta func saluda en este caso
        end = time.time()
        print("Despues de llamar la func")
        print(end-start)
    return envoltura

#usar @ -> seguido del nombre del decorador
@decorator
def saluda():
    print("Hola")
        
if __name__ == "__main__":
    saluda()
