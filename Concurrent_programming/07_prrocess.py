import os
from multiprocessing import Lock
from multiprocessing import Process


def info(title):
    print(title)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())


def f1(name):
    info("function f")
    print("hello", name)


def f2(lock, i):
    lock.acquire()
    try:
        print("hello world", i)
    finally:
        lock.release()


if __name__ == "__main__":
    info("main line")
    p = Process(target=f1, args=("bob",))
    p.start()
    p.join()

    lock = Lock()
    for num in range(10):
        Process(target=f2, args=(lock, num)).start()
