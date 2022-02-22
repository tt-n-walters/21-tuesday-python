import threading
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



start = time.time()

# slow_function("a")
# slow_function("b")
# slow_function("c")

threading.Thread(target=slow_function, args=("a", )).start()
threading.Thread(target=slow_function, args=("b", )).start()
threading.Thread(target=slow_function, args=("c", )).start()

end = time.time()
print("Took:", end - start)