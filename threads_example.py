from threading import Thread
import os
import time


def square_num():
    for i in range(100):
        i * i
        time.sleep(0.1)


threads = []

num_threads = 10

for t in range(num_threads):
    t = Thread(target=square_num)
    threads.append(t)

# Start
for t in threads:
    t.start()

# Join

for t in threads:
    t.join()


