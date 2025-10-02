list1 = [1, "abc", "abc", 1]

copy1 = list1.copy()
copy1.reverse()

if(copy1 == list1):
    print("Palindrome")
else:
    print("Not palindrome")