from time import *
from contextlib import contextmanager

class cm_timer1:
    def __init__(self):
        pass
    
    def __enter__(self):
       self.startTime = time()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
       print(time() - self.startTime)
 
@contextmanager
def cm_timer2():
    try:
        startTime = time()
        yield startTime
    finally:
        print(time() - startTime)
    
with cm_timer1():
    sleep(5.5)

with cm_timer2():
    sleep(5.5)