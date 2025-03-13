from multiprocessing import Process, Lock
import os
import time

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()    

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()