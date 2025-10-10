class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role=", self.role)
        print("dept=", self.dept)
        print("salary=", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 700000000)



e1 = Employee("Accountant", "Data Engineer", 60000000000)
e1.showDetails()

e2 = Engineer("Kajal", 22)
e2.showDetails()
