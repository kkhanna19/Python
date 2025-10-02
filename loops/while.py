count = 1
while count <=5 :
    print("hello")
    count += 1


i = 1
while i<=5 :
    print("hello", i)
    i += 1

i = 1
while i<=5 :
    print(i)
    i += 1


i = 5
while i>=1 :
    print(i)
    i -= 1


# print elements
list = [1, 4, 9, 16, 25, 36, 64, 81, 100]
heros = ["ironman", "thor", "superman", "batman"]

i = 0
while i < len(list):
    print(list[i])
    i += 1

i = 0
while i < len(heros):
    print(heros[i])
    i += 1

# print table
i = 1
n = int(input("enter num: "))
while i<=10:
    print(n,"x",i,"=",n*i)
    i += 1


# search x
list = [1, 4, 9, 16, 25, 36, 64, 81, 100] 
x = 16
i = 0
while i < len(list):
    if(list[i] == x):
        print("found at: ", i)
        break
    i += 1







