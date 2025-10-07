nums = [1, 3, 5, 6,7,8]

def print_len(nums):
    print(len(nums))

print_len(nums)


def print_list(nums): 
    for item in nums:
        print(item, end=" ")

print_list(nums)
print()

def fac(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact, end=" ")

fac(5)

