'''Yoy have been given an integer array/list of size N.
It contains 0s, 1s and 2s.
Write a solution to sort this array/list.'''

def sort012(arr,n):
    arr.sort()
    return arr

def sort_012(arr,n):
    zeros = arr.count(0)
    ones = arr.count(1)
    twos = arr.count(2)
    arr.clear()
    for i in range(zeros):
        arr.append(0)
    for i in range(ones):
        arr.append(1)
    for i in range(twos):
        arr.append(2)
    return arr

def sort__012(arr,n):
    start = 0
    middle = 0
    last = n - 1
    while middle <= last:
        if arr[middle] == 0:
            arr[middle] = arr[start]
            arr[start] = 0
            start += 1
            middle += 1
        elif arr[middle] == 1:
            middle += 1
        else:
            arr[middle] = arr[last]
            arr[last] = 2
            last -= 1
    return arr

def sort___012(arr,n):
    start = 0
    middle = 0
    last = n - 1
    while middle <= last:
        if arr[middle] == 0:
            arr[middle] = arr[start]
            arr[start] = 0
            start += 1
            middle += 1
        elif arr[middle] == 1:
            middle += 1
        else:
            arr[middle] = arr[last]
            arr[last] = 2
            last -= 1
    return arr

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    
    ans1 = sort012(arr,n)
    print(ans1)
    ans2 = sort_012(arr,n)
    print(ans2)
    ans3 = sort__012(arr,n)
    print(ans3)
    ans4 = sort___012(arr,n)
    print(ans4)