#!/usr/bin/python3


from multiprocessing import current_process
from multiprocessing import freeze_support
from multiprocessing import Process
from multiprocessing import Queue
from random import randrange
from time import time_ns
from time import time

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
        print(f"wrk proc: {current_process().name} takes:{func.__name__}({args})")
        result = calculate(func, args)
        output.put(result)

#
# Function used to calculate result
#
def calculate(func, args):
    result = asyncio.run(func(*args))
    print(f"wrk proc:{current_process().name} completed {func.__name__}{args} is {result}")
    return result


class dispatcher:
    def __init__(self, num_proc=NUM_OF_PROC):
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

    def allocate_task(self, single_task):
        self.task_queue.put(single_task)


    async def allocate_mul_task(self, task_list):
        #for func, args in task_list:
        for tsk in task_list:
            #self.task_queue.put((func, args))
            self.allocate_task(tsk)
            #print(f"Produced task: {func.__name__}{args}")
            await asyncio.sleep(0.1)


    async def collect_results(self):
        results = []
        for _ in range(self.result_queue.qsize()):
            while self.result_queue.empty():
                await asyncio.sleep(0.1)
                result = self.result_queue.get()                
                print(f"Consumed result:{result}")
                results.append(result)
        return results


    def stop_procs(self):
        for i in range(NUM_OF_PROC):
            self.task_queue.put("STOP")


    async def run(self, wkr):
        print("Processes started (Init)")
        for _ in range(self.num_of_proc):
            p = Process(target=wkr, args=(self.task_queue, self.result_queue))
            self.proclist.append(p)
            p.start()



async def asyncio_main():
    #task_queue = Queue()
    #result_queue = Queue()
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

    Producer = asyncio.create_task(MasterProc.allocate_mul_task(task_list))
    
    #MasterProc.allocate_mul_task(task_queue,task_list)

    await MasterProc.run(worker)

    await Producer

    MasterProc.stop_procs()

    results = await MasterProc.collect_results()

    for p in MasterProc.proclist:
        p.join()

    print(f"Tasks results:{results}")


if __name__ == "__main__":
    freeze_support()
    print("############ Dispatcher started ############")
    t1 = time()
    asyncio.run(asyncio_main())
    t2 = time()
    workingt_time = (t2 - t1)
    print(f"All tasks processed in :{workingt_time} s")    
    print("############ Dispatcher end  ############")
# MasterProc.shutdown()
