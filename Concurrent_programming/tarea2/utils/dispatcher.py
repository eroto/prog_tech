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


NUM_OF_PROC = 3


#
# Function run by worker processes
#
def worker(input, output):
    # print(current_process().name,end="==>")
    for func, args in iter(input.get, "STOP"):
        # print(f"func:{func.__name__} args:{args}")
        result = calculate(func, args)
        output.put(result)


#
# Function used to calculate result
#
def calculate(func, args):
    result = func(*args)
    return "%s says that %s%s = %s" % (
        current_process().name,
        func.__name__,
        args,
        result,
    )


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
            print("Other exception occurred")

    def allocate_task(self, single_task):
        self.task_queue.put(single_task)

    def allocate_mul_task(self, task_list):
        for tsk in task_list:
            self.allocate_task(tsk)

    def collect_results(self):
        for proc in self.proclist:
            if not proc.is_alive():
                print(f"result:{self.result_queue.get()}")
            else:
                print("Process are running")

    def fetch_task(self):
        pass

    def add_stop_signals(self):
        for i in range(NUM_OF_PROC):
            self.task_queue.put("STOP")

    def run(self, w):
        # self.add_stop_signals()
        print("Processes started (Init)")
        for i in range(self.num_of_proc):
            p = Process(target=w, args=(self.task_queue, self.result_queue))
            self.proclist.append(p)
            p.start()
        print("Processes started (End)")


"""
async def asyncio_main():
    async_tsk1 = asyncio.create_task(worker)
    await async_tsk1
"""

if __name__ == "__main__":
    freeze_support()

    t1 = time_ns()

    # Create master process
    MasterProc = dispatcher(3)
    print("############ Dispatcher started ############")
    print(f"Number of Processs:{MasterProc.num_of_proc}")
    # print(f"Task Queue size:{MasterProc.task_queue.qsize()}")

    task_list = []
    task_list = [(mul, (randrange(1, 10), randrange(1, 10))) for i in range(10)]
    task_list.append((mul, (23, 1981)))
    task_list.append((saluda, "E"))
    task_list.append((printer, "="))
    task_list.append((saluda, "P"))
    task_list.append((mul, (1977, 1981)))
    task_list.append((saluda, "S"))
    task_list.append((mul, (26, 95)))
    task_list.append((saluda, "R"))
    # task_list.append((sum, (23, 67)))

    # MasterProc.allocate_task(task2)
    # print(f"Task Queue size:{MasterProc.task_queue.qsize()}")

    MasterProc.allocate_mul_task(task_list)
    print(f"Task Queue size:{MasterProc.task_queue.qsize()}")

    # asyncio.run(asyncio_main())

    MasterProc.run(worker)

    # Get and print results
    print("Unordered results:")
    for i in range(len(task_list)):
        print("\t", MasterProc.result_queue.get())

    """
    for p in MasterProc.proclist:
        p.join()
        if p.is_alive():
            print(f"{p.name} timed out, terminating...")
            p.terminate()

    while not MasterProc.result_queue.empty():
        print(MasterProc.result_queue.get())'
    """

    # Tell child processes to stop
    for i in range(NUM_OF_PROC):
        MasterProc.task_queue.put("STOP")

    t2 = time_ns()
    workingt_time = (t2 - t1) / 1000000
    print(f"All tasks processed in :{workingt_time} ms")
print("############ Dispatcher end  ############")
# MasterProc.shutdown()
