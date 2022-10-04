# unique Element in the array

def uniqueElement(arr):
    
    uniqueElements = []  # if there are many unique element in the array
    for i in arr:
        if arr.count(i) == 1:
            uniqueElements.append(i)
    printArray(uniqueElements)

def uniqueElement1(arr):
    ans = 0
    for i in arr:
        ans = ans^i
    print(ans)

def printArray(arr):
    print(*arr)

size = int(input())
arr = list(map(int,input().split()))

uniqueElement(arr)
uniqueElement1(arr)

