from multiprocessing import Process
import os
import time


def square_num():
    for i in range(100):
        i * i
        time.sleep(0.1)


processes = []

num_process = os.cpu_count()

# Add process
for i in range(num_process):
    p = Process(target=square_num)
    processes.append(p)

# Run process
for p in processes:
    if __name__ == '__main__': # Using an if-statement to check if the module is the top-level environment and only starting child processes within that block will resolve the RuntimeError.
        p.start()

# Join
for p in processes:
    if __name__ == '__main__':
     p.join()
