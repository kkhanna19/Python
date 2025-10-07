f = open("demo.txt", 'r')
data = f.read()
print(data)
print(type(data))
f.close()
print()


f = open("demo.txt", 'r')
data = f.read(5)
print(data)
f.close()
print()

f = open("demo.txt", 'r')
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()


# write
f = open("demo.txt", 'w')
f.write("This is new line")
f.close()

f = open("demo.txt", 'a')
f.write("\nI'll come by next week")
f.close()


f = open("sample.txt", 'w')
f.close()


f = open("demo.txt", 'r+')    #-> no truncate p=start
f.write("I'll come by next week")
f.close()


f = open("demo.txt", 'w+')    #truncate p=end
f.write("I'll come by next week")
f.close()


f = open("demo.txt", 'a+')   #no truncate  p=end
f.write("I'll come by next week")
f.close()


