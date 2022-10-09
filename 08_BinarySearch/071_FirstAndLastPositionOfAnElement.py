'''You have been given sorted array/list consisting of N elements.
You are also given an iinteger K.
Now your task is to find the first and last occurance of k in arr.'''


def firstOccurance(arr,n,key):
    start = 0
    end = n-1
    mid = start + (end-start)//2
    ans = -1
    while start<=end:
        if arr[mid] == key:
            ans = mid
            end = mid - 1
            mid = start + (end-start)//2
        elif key > arr[mid]:
            start = mid + 1
            mid = start + (end-start)//2
        elif key < arr[mid]:
            end = mid - 1
            mid = start + (end-start)//2
    return ans

def lastOccurance(arr,n,key):
    start = 0
    end = n-1
    mid = start + (end-start)//2
    ans = -1
    while start<=end:
        if arr[mid] == key:
            ans = mid
            start = mid + 1
            mid = start + (end-start)//2
        elif key > arr[mid]:
            start = mid + 1
            mid = start + (end-start)//2
        elif key < arr[mid]:
            end = mid - 1
            mid = start + (end-start)//2
    return ans

def firstAndLastPosition(arr,n,key):
    
    ans1 = firstOccurance(arr,n,key)
    ans2 = lastOccurance(arr,n,key)
    return ans1,ans2


if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        n = int(input())
        arr = list(map(int,input().split()))
        k = int(input())

        ans = firstAndLastPosition(arr,n,k)
        print(ans)