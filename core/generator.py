

def naive_function():
    numbers = []
    for i in range(50_000_000):
        numbers.append(i)
    return numbers


def lazy_function():
    for i in range(50_000_000):
        yield i


memory = lazy_function()

total = 0
for n in memory:
    total += n
print("total = ", total)
