a = 9
b = 5
c = 6

if(a > b and a > c):
    print("a")
elif(b > a and b > c):    #elif(b>c)  bcoz if is wrong a is not greatest
    print("b")
else:
    print("c")



#greatest of 4
a = 4
b = 7
c = 0
d = 5

if(a > b and a > c and a > d):
    print("a")
elif(b > c and b > d):    
    print("b")
elif(c > d):    
    print("c")
else:
    print("d")