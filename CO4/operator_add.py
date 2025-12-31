
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def total(self):
        return self.m1 + self.m2
    def __add__(self, other):
        return self.total() + other.total()
