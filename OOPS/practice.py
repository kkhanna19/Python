class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def avg(self):
       sum = 0
       for val in self.marks:
           sum +=  val
       print("hi", self.name, "ur avg marks:", sum/3)

s1 = Student("kajal", [89,78,65])
print(s1.name, s1.marks)
s1.avg()
s1.hello()

s1.name = "karan"   # chng name 
s1.avg()