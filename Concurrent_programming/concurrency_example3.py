#!/usr/bin/python3

#execute several corroutines concurrently

import concurrent.futures
import time
import random

#global variable!

shared_counter = 0

def increment(data):
    time.sleep(random.uniform(0,0.1))
    print(f"data:{data}")
    result = data + 1
    print(f"result:{result}")
    return result

def apply_fnc_concurrently(fnc, data):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = list(executor.map(fnc, data))
    aggregated_result = sum(result)
    return aggregated_result

if __name__== "__main__":
    data = [0] * 100
    shared_counter = apply_fnc_concurrently(increment,data)
    print(f"final value {shared_counter}")