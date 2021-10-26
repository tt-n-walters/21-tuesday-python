

def function():
    print("Hello, world!")
    return 123456


# result = function()
# print(result)
str

class A:
    def __repr__(self):   # Representation
        return "This works!"
    
    def __add__(self, other):
        print("Adding?")
        return "This works" + str(other)
    
    def __call__(self, *args):
        import random
        print("Hi there.")
        return random.randint(1, 100)

a = A()

print(function)
print(a)


x = a + 20

print(type("hello world"))
print(type(123))


print(a())