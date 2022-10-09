def binarySearch(arr,size,key):
    start = 0
    end = size - 1
    mid = start + (end-start)//2

    while start<=end:
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            start = mid + 1
            mid = start + (end-start)//2
        else:
            end = mid - 1
            mid = start + (end-start)//2
    return -1

if __name__ == "__main__":
    even = [2,4,6,8,12,18]
    odd = [3,8,11,14,16]

    evenIndex = binarySearch(even,len(even),20)
    print('index of 20 is',evenIndex)

    oddIndex = binarySearch(odd,len(odd),8)
    print('index of 8 is',oddIndex)