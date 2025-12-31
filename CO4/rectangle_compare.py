
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
    def __lt__(self, other):
        return self.area() < other.area()
