#!/usr/bin/python3


from multiprocessing import current_process
from multiprocessing import freeze_support
from multiprocessing import Process
from multiprocessing import Queue
from random import randrange
from time import time_ns

from operations import mul
from operations import printer
from operations import saluda

import asyncio

NUM_OF_PROC = 3

#
# Function run by worker processes
#
def worker(input, output):
    #print(current_process().name,end="==>")
    for func, args in iter(input.get,"STOP"):
        print(f"wrk c p: {current_process().name}")
        result = calculate(func, args)
        output.put(result)

    '''
    for func, args in iter(input.get, "STOP"):
        print(f"func:{func.__name__} args:{args}")
        result = calculate(func, args)
        output.put(result)
    '''


#
# Function used to calculate result
#
def calculate(func, args):
    result = func(*args)
    print(f"{current_process().name} says {func.__name__}{args} is {result}")
    return result


class dispatcher:
    def __init__(self, num_proc=NUM_OF_PROC):
        if num_proc > 0:
            try:
                self.num_of_proc = num_proc
                #self.task_queue = Queue()
                #self.result_queue = Queue()
                self.proclist = []
            except ValueError as e:
                print("An exception occurred: {e}")
        else:
            print("Other exception occurred")

    async def allocate_task(self, tq, single_task):
        tq.put(single_task)

    async def allocate_mul_task(self, tq, task_list):
        #for tsk in task_list:
        #    await self.allocate_task(tq, tsk)
        for func, args in task_list:
            tq.put((func, args))
        
        await asyncio.sleep(0.1)

    async def collect_results(self, tq, rq):
        results = []
        for _ in range(tq.qsize()):
            while rq.empty():
                await asyncio.sleep(0.1)
                result = rq.get()                
                print(f"Consumed result:{result}")
                results.append(result)

    def fetch_task(self):
        pass

    def add_stop_signals(self, tq):
        for i in range(NUM_OF_PROC):
            tq.put("STOP")

    def run(self, tq, rq, wkr):
        # self.add_stop_signals()
        print("Processes started (Init)")
        for i in range(self.num_of_proc):
            p = Process(target=wkr, args=(tq, rq))
            self.proclist.append(p)
            p.start()



async def asyncio_main():
    task_queue = Queue()
    result_queue = Queue()
    task_list = []

    # Create master process
    MasterProc = dispatcher(3)
    print(f"Number of Processs:{MasterProc.num_of_proc}")

    
    #task_list = [(mul, (randrange(1, 10), randrange(1, 10))) for i in range(10)]
    task_list.append((saluda, "E"))
    task_list.append((mul, (26, 95)))
    task_list.append((printer, "="))
    task_list.append((saluda, "P"))
    task_list.append((mul, (1977, 1981)))
    task_list.append((saluda, "S"))
    task_list.append((mul, (26, 95)))
    task_list.append((saluda, "R"))
    print(f"Num Tasks: {len(task_list)}")

    #for tsk in task_list:
    #    task_queue.put(tsk)
    
    Producer = asyncio.create_task(MasterProc.allocate_mul_task(task_queue,task_list))

    print(f"Task Queue size:{task_queue.qsize()}")
    
    # asyncio.run(asyncio_main())

    MasterProc.run(task_queue, result_queue, worker)

    await Producer

    # Tell child processes to stop
    for i in range(NUM_OF_PROC):
        task_queue.put("STOP")

    #results = await MasterProc.collect_results(task_queue, result_queue)

    for p in MasterProc.proclist:
        p.join()
'''
    # Get and print results
    print("Unordered results:")
    for i in range(len(task_list)):
        print("\t", MasterProc.result_queue.get())
'''


if __name__ == "__main__":
    freeze_support()
    print("############ Dispatcher started ############")
    t1 = time_ns()
    asyncio.run(asyncio_main())
    t2 = time_ns()
    workingt_time = (t2 - t1) / 1000000
    print(f"All tasks processed in :{workingt_time} ms")    
    print("############ Dispatcher end  ############")
# MasterProc.shutdown()
