from multiprocessing import Process, Pool,cpu_count
import time
import os
import timer

t = timer.Timer()

def cube(x):
    return x*x*x


if __name__ == '__main__':

    t.start_timer()
    for i in range(50000000):
        cube(i)
    t.stop_timer()

    with Pool() as pool:
        t.start_timer()
        res = pool.map(cube,range(0,50000000))
        t.stop_timer()
        #print(res)