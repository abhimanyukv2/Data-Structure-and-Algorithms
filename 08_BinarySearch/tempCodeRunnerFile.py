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

arr = [1,2,3,3,5]
n = 5
k = 3
ans = firstOccurance(arr,n,k)
print(ans)