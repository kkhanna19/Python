with open("practice.txt", 'r')as f:
    data = f.read()
    print(data)
     
num = ""
for i in range(len(data)):
    if(data[i] == ","):
        print(int(num))
        num = ""
    else:
        num += data[i]


cnt = 0
with open("practice.txt", 'r')as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            cnt += 1
    
print(cnt)
            
