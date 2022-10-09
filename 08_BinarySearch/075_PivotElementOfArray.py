'''Pivot element of an array
pivot element is the element which is smallest or largest
element in the array.'''

def pivotElement(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        mid = start + (end - start)//2

        if arr[mid] >= arr[0]:
            start = mid + 1
        else:
            end = mid

    return start

if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        arr = list(map(int,input().split()))

        ans1 = pivotElement(arr)
        print(ans1)