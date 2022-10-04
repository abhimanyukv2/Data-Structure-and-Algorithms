# duplicate Element in the array

def duplicateElement(arr):
    
    duplicateElements = []  # if there are many unique element in the array
    for i in arr:
        if arr.count(i) > 1 and i not in duplicateElements:
            duplicateElements.append(i)
    printArray(duplicateElements)

def duplicateElement1(arr):
    ans = 0
    for i in arr:
        ans = ans^i
    for i in range(1,len(arr)):
        ans = ans^i
    print(i)

def findDuplicates(self, nums: list[int]) -> list[int]:
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    arr = []
    for i in dic:
        if dic[i] > 1:
            arr.append(i)
    arr.sort()
    return arr

def findDuplicates1(self, nums):
    ans = []
    for num in nums:
        if nums[abs(num)-1] < 0:
            ans.append(abs(num))
        else:
            nums[abs(num)-1] *= -1
    return ans

def printArray(arr):
    print(*arr)

size = int(input())
arr = list(map(int,input().split()))

duplicateElement(arr)
duplicateElement1(arr)
findDuplicates(arr)
findDuplicates1(arr)