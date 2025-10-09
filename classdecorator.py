class Person:
    name = "kajal"

    # def changeName(self, name):
    #     self.__class__.name = "rahul"
    #     Person.name = "rahul"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("rahul")
print(p1.name)
# print(Person.name)
