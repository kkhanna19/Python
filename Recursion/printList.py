def print_list(list, idx=0):   # 0 -> is default value
    if(idx == len(list)):
        return
    print(list[idx], end=" ")
    print_list(list, idx+1)

fruits = ["apple", "banana", "mango", "beetroot"]

print_list(fruits)