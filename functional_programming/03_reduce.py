#!/usr/bin/python3
from functools import reduce


# entry point
if __name__ == "__main__":
    # lista numeros
    numbers = [1, 2, 3, 4, 5]

    total = reduce(lambda x, y: x + y, numbers)
    print(total)
