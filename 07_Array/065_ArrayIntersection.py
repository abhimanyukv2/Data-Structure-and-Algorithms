# array intersection

def arrayIntersection(arr,brr):
    intersection = []
    for i in arr:
        if i in brr:
            intersection.append(i)
    printArray(intersection)

def printArray(arr):
    print(*arr)

sizeofArr = int(input())
sizeofBrr = int(input())

arr = list(map(int,input().split()))
brr = list(map(int,input().split()))

arrayIntersection(arr,brr)