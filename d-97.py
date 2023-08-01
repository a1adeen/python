# multithreading
import threading
import time

def func(sec):
    print(f"sleeping for {sec} seconds")
    time.sleep(sec)
    print("hey")
# normal code
func(2)
func(3)
func(2)
# same code using threading
# with this we can do several tasks at the time
t1 = threading.Thread(target=func, args=[3])
t2 = threading.Thread(target=func, args=[32])
t3 = threading.Thread(target=func, args=[2])

t1.start()
t2.start()
t3.start()