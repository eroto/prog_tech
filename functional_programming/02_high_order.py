#!/usr/bin/python3


# entry point
if __name__ == "__main__":

    #lista de palabras
    palabras={"arbol","casa","automovil","ciudad","programacion"}

    #high order function "filter" -> select words with more than 5 letters
    result = filter(lambda palabra: len(palabra)>5, palabras)
    #result = list(result)
    print(list(result))

