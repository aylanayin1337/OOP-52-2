class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"-> Прямоугольник ({self.width}, {self.height})"

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

r1 = Rectangle(4, 5)
r2 = Rectangle(3, 6)

print(r1)
print(r2)
print("---------------")

print(r1.area())
print(r2.area())
print("---------------")

print(r1 == r2)
print(r1 > r2)
print(r1 < r2)

