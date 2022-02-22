


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)



if __name__ == "__main__":
    a = Vector(x=1, y=2)
    b = Vector(x=8, y=9)

    c = a + b
    print(a, "+", b)
    print(c)