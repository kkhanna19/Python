info ={
    "key" : "value",
    "name" : "kajal",
    "age" : 22,
    "subject" : ["python", "java", "sql"],
    "marks" : (67, 45, 91),
    89 : "kajal"
}

print(type(info))

print(info["marks"])
print(info["name"])
print(info["subject"])


# assign value
info["name"] = "kajal"

print(info)

# add value
info["surname"] = "khanna"
print(info)

null = {}
print(null)

#nested dictionary
student = {
    "name" : "kajal",
    "subjects" : {
        "phy" : 90,
        "chem" : 56,
        "math" : 97
    }
}

print(student)
print(student["subjects"]["chem"])

print(student.keys())
print(list(student.keys()))
print(len(student))

print(student.values())

print(student.items())

pair = list(student.items())
print(pair[0])

# print(student["name2"])   --> it gives error
print(student.get("name2"))

student.update({"city" : "jaipur"})
print(student)

new = {"age" : 22}
student.update(new)
print(student)