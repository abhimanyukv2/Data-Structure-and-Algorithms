# array with functon

def printArray(arr,size):
    print('Printing the array')
    for i in range(size):
        print(arr[i])
    print('printing done')
size = int(input())
arr = []
for i in range(size):
    arr.append(input())
printArray(arr,size)


# length of an array
length = len(arr)
print(length)