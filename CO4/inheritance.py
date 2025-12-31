
class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Name =", self.name)

class MCAStudent(Student):
    def __init__(self, name, sem):
        super().__init__(name)
        self.sem = sem
    def show_details(self):
        self.display()
        print("Semester =", self.sem)
