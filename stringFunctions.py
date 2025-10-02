str = "kajal khanna"
print(str.endswith("nna"))

print(str.capitalize())   #--> it works only for the first time  or in new string not in original 
print(str)  #--> it prints the original str

str = str.capitalize()   #--> for permanent or in original
print(str)

print(str.replace("Kajal", "kaju"))
print(str.replace("a", "m"))


print(str.find("a"))  #print index of 1st time occur 
print(str.find("v"))
print(str.find("kh"))

print(str.count("a"))

name = input("your name: ")
print(len(name))