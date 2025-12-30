import threading
import time

class SharedCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        self._lock.acquire()
        try:
            temp = self.value
            time.sleep(0)
            self.value = temp + 1
        finally:
            self._lock.release()


counter = SharedCounter()
ITERATIONS = 10000
THREADS = 5

def worker():
    for _ in range(ITERATIONS):
        counter.increment()

threads = []

for _ in range(THREADS):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

expected = ITERATIONS * THREADS
print("Expected:", expected)
print("Actual:  ", counter.value)
