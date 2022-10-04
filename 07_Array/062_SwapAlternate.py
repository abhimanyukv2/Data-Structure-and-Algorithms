# swap alternate

def swapAlternate(arr,size):
    if size%2 != 0:
        size = size - 1
    for i in range(0,size,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]

def printArray(arr):
    for i in arr:
        print(i,end=' ')
    print()

sizeofArr = int(input())
sizeofBrr = int(input())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))

swapAlternate(arr,sizeofArr)
swapAlternate(brr,sizeofBrr)

printArray(arr)
printArray(brr)