import multiprocessing
import time
import hashlib


memory = list(range(30_000_000))


def function(name):
    for i in range(10):
        print("Current:", name, i)
        time.sleep(1)


def slow_function(name):
    for i in range(10):
        print("Current:", name, i)
        for j in range(300_000):
            hashlib.md5(str(j).encode("utf-8")).hexdigest()



if __name__ == "__main__":
    for i in range(3):
        name = chr(97 + i)
        multiprocessing.Process(target=slow_function, args=(name, )).start()
