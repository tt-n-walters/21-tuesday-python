import hashlib
from os import path
import time
import itertools
root = path.abspath(path.dirname(__file__))

def hash_text(plaintext):
    return hashlib.md5(plaintext.encode()).hexdigest()


def variations(password):
    options = []
    try:
        for password in (password, password[0].upper() + password[1:]):
            options.append(password)
            for i in range(10):
                p = f"{password}{i}"
                options.append(p)
    finally:
        return options


def read_passwords():
    file = open(file_path, "r", encoding="utf-8")
    for line in file:
        yield line.strip()


target = "ae934c69d85fe3a4d9b27a4b96b00862"
filename = "rockyou.txt"
file_path = path.join(root, filename)


start = time.time() - 0.001
num_hashed = 0

def crack_passwords(start_index, stop_index):
    global num_hashed

    passwords = itertools.islice(read_passwords(), start_index, stop_index)

    for i, password in enumerate(passwords):
        options = variations(password)
        
        if i % 1000 == 0:
            rate = num_hashed / (time.time() - start)
            print("  Checked {} passwords   Rate: {:.2f}".format(num_hashed, rate), end="\r")

        match_found = False

        for p in options:
            hashed = hash_text(p)
            num_hashed += 1
            if hashed == target:
                print("Found match.", p)
                match_found = True
                break
        
        if match_found:
            break

    else:
        print("\nNo matches found.")


import multiprocessing

if __name__ == "__main__":
    num_of = 14_344_390

    multiprocessing.Process(target=crack_passwords, args=(0, num_of//4)).start()
    multiprocessing.Process(target=crack_passwords, args=(num_of//4, num_of//4*2)).start()
    multiprocessing.Process(target=crack_passwords, args=(num_of//4*2, num_of//4*3)).start()
    multiprocessing.Process(target=crack_passwords, args=(num_of//4*3, num_of)).start()
