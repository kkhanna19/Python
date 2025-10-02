marks = [12, 24, 45.6, 43, 45.45]   #store diff types of elements but not in others
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

# list is immutable
student = ["kajal", 98.9, "jaipur"]
print(student)
student[0] = "khanna"
print(student)


#list slicing
print(marks[1:4])     #ending is not included
print(marks[0:])
print(marks[:4])

print(marks[-4: -1])
