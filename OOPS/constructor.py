class Student:
    college = "ABC college"    #common or class variable which is shared among all

    # deafult constructor
    def __init__(self):
        pass  

    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name    # obj attr > class attr
        self.marks = marks
        print("adding new Student...")

s1 = Student("karan", 78)
print(s1.name, s1.marks)
print(s1.college)

s2 = Student("kajal", 98)
print(s2.name, s2.marks)
print(s2.college)

print(Student.college)
