#!/usr/bin/python3


from multiprocessing import current_process
from multiprocessing import freeze_support
from multiprocessing import Process
from multiprocessing import Queue
from random import randrange
from time import time_ns
from time import time

import asyncio



'''
Name: worker
Desc: Executes tasks retrieved from the input queue until the "STOP" signal is encountered.
    Processes tasks using the `calculate` function and puts the results into the output queue.
'''
def worker(input, output):
    #print(current_process().name,end="==>")
    for func, args in iter(input.get,"STOP"):
        print(f"wrk proc: {current_process().name} fetchs:{func.__name__}({args})")
        result = calculate(func, args)
        output.put(result)

'''
Name: calculate
Desc: Runs an asynchronous function (`func`) with the provided arguments (`args`)
'''
def calculate(func, args):
    result = asyncio.run(func(*args))
    print(f"wrk proc:{current_process().name} completed {func.__name__}{args} is {result}")
    return result

'''
Name: dispatcher (class)
Desc: A class that manages task distribution among multiple processes.
    It initializes task and result queues, processes, and supports task allocation,
    results collection, and process management.
'''
class dispatcher:
    '''
    Name:__init__
    Desc: Initializes the dispatcher instance.
        Sets up the number of processes (`num_proc`), task and result queues, and a list to track processes.
    '''
    def __init__(self, num_proc=1):
        if num_proc > 0:
            try:
                self.num_of_proc = num_proc
                self.task_queue = Queue()
                self.result_queue = Queue()
                self.proclist = []
            except ValueError as e:
                print("An exception occurred: {e}")
        else:
            print("Num of process  shall be >= 1")

    '''
    Name: allocate_task
    Desc: Adds a single task to the task queue.
    '''
    def allocate_task(self, single_task):
        self.task_queue.put(single_task)

    '''
    Name: allocate_mul_task
    Desc: Asynchronously adds multiple tasks from a list to the task queue, introducing a brief delay (`asyncio.sleep`) between task additions.
    '''
    async def allocate_mul_task(self, task_list):
        #for func, args in task_list:
        for tsk in task_list:
            #self.task_queue.put((func, args))
            self.allocate_task(tsk)
            #print(f"Produced task: {func.__name__}{args}")
            await asyncio.sleep(0.1)

        '''
        Name: collect_results
        Desc: Asynchronously collects results from the result queue. Waits if the queue is empty and continues until all results are retrieved.
        '''
    async def collect_results(self):
        results = []
        for _ in range(self.result_queue.qsize()):
            while self.result_queue.empty():
                await asyncio.sleep(0.1)
                result = self.result_queue.get()                
                print(f"Consumed result:{result}")
                results.append(result)
        return results

    '''
    Name: stop_procs

    Desc: Sends the "STOP" signal to each process in the queue to gracefully stop them.
    '''
    def stop_procs(self):
        for i in range(self.num_of_proc):
            self.task_queue.put("STOP")

    '''
    Name: run
    Desc: Starts the specified number of processes (`num_proc`) using the provided worker function (`wkr`).
    Processes are added to the internal process list and started.
    '''
    async def run(self, wkr):
        print("Processes started (Init)")
        for _ in range(self.num_of_proc):
            p = Process(target=wkr, args=(self.task_queue, self.result_queue))
            self.proclist.append(p)
            p.start()
