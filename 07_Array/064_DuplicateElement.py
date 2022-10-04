# duplicate Element in the array

def duplicateElement(arr):
    
    duplicateElements = []  # if there are many unique element in the array
    for i in arr:
        if arr.count(i) > 1 and i not in duplicateElements:
            duplicateElements.append(i)
    printArray(duplicateElements)



def printArray(arr):
    print(*arr)

size = int(input())
arr = list(map(int,input().split()))

duplicateElement(arr)
