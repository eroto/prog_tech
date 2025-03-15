import random
import time
from multiprocessing import current_process
from multiprocessing import freeze_support
from multiprocessing import Process
from multiprocessing import Queue

#
# Function run by worker processes
#


def worker(input, output):
    t1 = time.time() * 1000
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


#
# Functions referenced by tasks
#


def mul(a, b):
    time.sleep(0.5 * random.random())
    return a * b


def plus(a, b):
    time.sleep(0.5 * random.random())
    return a + b


#
#
#


def test():
    NUMBER_OF_PROCESSES = 6
    TASKS1 = [(mul, (i, 7)) for i in range(20)]
    TASKS2 = [(plus, (i, 8)) for i in range(10)]

    # Create queues
    task_queue = Queue()
    done_queue = Queue()

    # Submit tasks
    for task in TASKS1:
        task_queue.put(task)

    print(f"Task queue length: {task_queue.qsize()}")
    print(f"Result queue length: {done_queue.qsize()}")

    # Start worker processes
    for i in range(NUMBER_OF_PROCESSES):
        print(f"Process #{i} created")
        Process(target=worker, args=(task_queue, done_queue)).start()

    # Get and print results
    print("Unordered results:")
    for i in range(len(TASKS1)):
        print("\t", done_queue.get())

    # Add more tasks using `put()`
    for task in TASKS2:
        task_queue.put(task)

    # Get and print some more results
    for i in range(len(TASKS2)):
        print("\t", done_queue.get())

    # Tell child processes to stop
    for i in range(NUMBER_OF_PROCESSES):
        task_queue.put("STOP")


if __name__ == "__main__":
    freeze_support()
    test()
