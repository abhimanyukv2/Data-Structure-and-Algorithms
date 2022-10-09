'''Counting total number of occurance of an element
in an sorted array using binary search.'''


def firstOcuurance(arr,size,key):
    start = 0
    end = size - 1
    mid = start + (end-start)//2
    first = -1
    while start<=end:
        if arr[mid] == key:
            first = mid
            end = mid - 1
        elif arr[mid]<key:
            start = mid + 1
        elif arr[mid]>key:
            end = mid - 1

        mid = start + (end - start)//2
    return first

def lastOccurance(arr,size,key):
    start = 0
    end = size - 1
    mid = start + (end - start)//2
    last = -1
    while start<=end:
        if arr[mid] == key:
            last = mid
            start = mid + 1
        elif arr[mid]<key:
            start = mid + 1
        elif arr[mid]>key:
            end = mid - 1

        mid = start + (end - start)//2
    return last

def totalNumberOfOccurance(arr,size,key):
    firstPosition = firstOcuurance(arr,size,key)
    lastPosition = lastOccurance(arr,size,key)

    NumberOfOccurance = lastPosition - firstPosition + 1

    return NumberOfOccurance


if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        size = int(input())
        arr = list(map(int,input().split()))
        key = int(input())

        ans = totalNumberOfOccurance(arr,size,key)
        print(ans)

    