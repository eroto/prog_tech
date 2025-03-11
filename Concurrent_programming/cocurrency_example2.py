#!/usr/bin/python3

#execute several corroutines concurrently

import concurrent.futures
import time
import random

#global variable!

shared_counter = 0

def increment_counter():
    global shared_counter
    current_value =  shared_counter
    time.sleep(random.uniform(0, 0.1))
    shared_counter = current_value + 1
    return shared_counter

def run_concurrently(num_times):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures  = [executor.submit(increment_counter) for _ in range(num_times)]
    concurrent.futures.wait(futures)

if __name__== "__main__":
    run_concurrently(100)
    print(f"final value {shared_counter}")