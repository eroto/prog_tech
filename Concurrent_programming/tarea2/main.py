#!/usr/bin/python3
from multiprocessing import current_process
from multiprocessing import freeze_support
from multiprocessing import Process
from multiprocessing import Queue
from random import randrange
from time import time_ns
from time import time
from utils.dispatcher import dispatcher
from utils.dispatcher import worker
from utils.dispatcher import calculate
from utils.operations import mul
from utils.operations import printer
from utils.operations import saluda
import asyncio


NUM_OF_PROC = 3

'''
Name: asyncio_main
Desc: Main corutine, creates the dispatcher object with the number of processes as input, creates a task list,
    allocote tasks in the task que and start the dispatcher that fetch tasks from the task queue until all completed
'''
async def asyncio_main():
    #task_queue = Queue()
    #result_queue = Queue()
    task_list = []

    # Create master process
    MasterProc = dispatcher(NUM_OF_PROC)
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