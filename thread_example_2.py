# Race condition
from threading import Lock, Thread
import time

database_value = 0


"""def increment(lock_obj):
    global database_value
    lock_obj.acquire()
    local_value = database_value
    local_value += 1
    time.sleep(0.1)
    database_value = local_value
    lock_obj.release() """


def increment(lock_obj):
    global database_value
    with lock_obj:
        local_value = database_value
        local_value += 1
        time.sleep(0.1)
        database_value = local_value


if __name__ == "__main__":
    lock = Lock()
    t1 = Thread(target=increment, args=(lock,))
    t2 = Thread(target=increment, args=(lock,))

    print(f"start value {database_value}")
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"End value {database_value}")
