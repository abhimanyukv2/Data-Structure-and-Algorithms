# Reverse an array

def reverse(arr):
    start = 0
    end = len(arr)-1
    while start<=end:
        arr[start],arr[end] = arr[end],arr[start]
        start = start + 1
        end -= 1


def printArray(arr):
    for i in arr:
        print(i,end=' ')
    print()

arr = [1,4,0,5,-2,15]
brr = [2,6,3,9,4]

reverse(arr)
reverse(brr)

printArray(arr)
printArray(brr)