nums =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


for i in nums:
    print(i)


nums =(1, 4, 9, 16, 25, 36, 49, 64, 81, 100,49)

x = 49
idx = 0
for i in nums:
    if(i == x):
        print("num found at idx:", idx) 
        break
    idx += 1
