# print sum of all element

# using function
def sumOfArray(arr,size):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

size = int(input())
arr = [int(value) for value in input().split()]
print(sumOfArray(arr,size))

# using built in function
print(sum(arr))