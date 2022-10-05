# Intersection Of Two Sorted Arrays

def arrayIntersection(arr,brr):
    intersection = []
    i = 0
    j = 0
    while True:
        if arr[i] > brr[j]:
            j = j + 1
        elif arr[i] < brr[j]:
            i = i + 1
        else:
            intersection.append(arr[i])
            i = i + 1
            j = j + 1
        
        if i == len(arr) or j == len(brr):
            printArray(intersection)
            break

def printArray(arr):
    print(*arr)

sizeofArr = int(input())
sizeofBrr = int(input())

arr = list(map(int,input().split()))
brr = list(map(int,input().split()))

arrayIntersection(arr,brr)