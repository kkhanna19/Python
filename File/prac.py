with open("practice.txt", 'w')as f:
    f.write("hello everyone, \nwe are learning Python")
    f.write("\ntopic is I/O")


with open("practice.txt", 'r') as f:
    data = f.read()
    print(data)

new_data = data.replace("Python", "JAVA")
print(new_data)

with open("practice.txt", 'w')as f:
    f.write(new_data)

def check():
    word = "learning"
    with open("practice.txt", 'r')as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")

check()


def checkLine():
    word = "learning"
    data = True
    line = 1
    with open("practice.txt", 'r') as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line)
                return
            line += 1
    return -1
checkLine()








