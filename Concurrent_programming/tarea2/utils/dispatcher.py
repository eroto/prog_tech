#!/usr/bin/python3


from multiprocessing import current_process
from multiprocessing import freeze_support
from multiprocessing import Process
from multiprocessing import Queue
from random import random
from random import randrange
from time import sleep
from time import time


NUM_OF_PROC = 4


#
# Function run by worker processes
#


def worker(input, output):
    t1 = time() * 1000
    print(current_process().name)
    print(f"Worker start time:{t1}")
    for func, args in iter(input.get, "STOP"):
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


def mul(a, b):
    sleep(2.5 * randrange(1,2))
    return a * b


class dispatcher:
    def __init__(self, num_proc=NUM_OF_PROC):
        if num_proc > 0:
            try:
                self.num_of_proc = num_proc
                self.task_queue = Queue()
                self.result_queue = Queue()
                self.proclist = []
            except:
                print("An exception occurred")
        else:
            print("Other exception occurred")

    def allocate_task(self, single_task):
        self.task_queue.put(single_task)

    def allocate_mul_task(self, task_list):
        for tsk in task_list:
            self.allocate_task(tsk)

    def collect_results(self):
        for proc in self.proclist:
            if proc.is_alive() == False:
                print(f"result:{self.result_queue.get()}")
            else:
                print("Process are running")

    def fetch_task():
        pass

    def add_stop_signals(self):
        for i in range(NUM_OF_PROC):
            self.task_queue.put("STOP")

    def run(self, w):
        self.add_stop_signals()
        for i in range(self.num_of_proc):
            p = Process(target=w, args=(self.task_queue, self.result_queue))
            self.proclist.append(p)
            p.start()


if __name__ == "__main__":
    freeze_support()

    # Create master process
    MasterProc = dispatcher(2)
    print(f"Number of Processs:{MasterProc.num_of_proc}")
    print(f"Task Queue size:{MasterProc.task_queue.qsize()}")

    task_list = [(mul, (randrange(1, 10), randrange(1, 10))) for i in range(5)]
    task2 = (mul, (23, 1981))

    MasterProc.allocate_task(task2)
    print(f"Task Queue size:{MasterProc.task_queue.qsize()}")
    MasterProc.allocate_mul_task(task_list)
    print(f"Task Queue size:{MasterProc.task_queue.qsize()}")

    MasterProc.run(worker)

    for p in MasterProc.proclist:
        p.join(5)
        if p.is_alive():
            print(f"{p.name} timed out, terminating...")
            p.terminate()

    while not MasterProc.result_queue.empty():
        print(MasterProc.result_queue.get())

    print("All tasks processed.")

    # MasterProc.shutdown()
