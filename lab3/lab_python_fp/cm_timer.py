from time import *
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        pass
    
    def __enter__(self):
       self.startTime = time()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
       print("time {}".format(time() - self.startTime))
 
@contextmanager
def cm_timer_2():
    try:
        startTime = time()
        yield startTime
    finally:
        print("time {}".format(time() - startTime))

if __name__ == "__main__":
    with cm_timer_1():
        sleep(3.5)
    
    with cm_timer_2():
        sleep(2)