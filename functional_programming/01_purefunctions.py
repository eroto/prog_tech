#!/usr/bin/python3

#pure function + first order
def factorial(number):
    if number in (0,1):
        return 1
    else:
        return number * factorial(number-1)

#higher-Order Functions

# entry point
if __name__ == "__main__":
    print(f"{factorial(5)=}")

    '''
    numbers = [1,2,3,4,5]
    sq_numbers = map(lambda x : x**2,numbers)
    print(sq_numbers.__next__)
