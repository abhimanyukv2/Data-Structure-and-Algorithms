'''You have been given a sorted array consisting of N element.
You are also given an integer K. Now the array is rotated
at some point unknown to you.Now your task is to find
the index at which K is present in array.'''


def pivotPosition(arr,n):
    start = 0
    end = n - 1

    while start < end:
        mid = start + (end - start)//2
        
        if arr[mid] >= arr[0]:
            start = mid + 1
        else:
            end = mid
    # print(start)
    return start


def findPosition(arr,n,k):
    pivot = pivotPosition(arr,n)
    if arr[pivot] <= k and arr[n-1] >= k:
        start = pivot
        end = n - 1
    else:
        start = 0
        end = pivot - 1
    # print(start,end)
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid - 1
        elif arr[mid] < k:
            start = mid + 1

    return -1


if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        n = int(input())
        arr = list(map(int,input().split()))
        k = int(input())

        ans = findPosition(arr,n,k)
        print(ans)