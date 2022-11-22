'''Given a sequence of integers , a triplet (a[i], a[j], a[k])
is beautiful if:
* i < j < k
* a[j] - a[i] == a[k] - a[j] == d
Given an increasing sequenc of integers and the value of,
count the number of beautiful triplets in the sequence.'''

#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulTriplets(d, arr):
    # Write your code here
    ans = 0
    for i in arr:
        j = i + d
        k = i + 2*d

        if isPresent(j, arr) and isPresent(k, arr):
            ans += 1
    
    return ans

def isPresent(element,arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start)//2

        if arr[mid] == element:
            return True
        elif arr[mid] < element:
            start = mid + 1
        elif arr[mid] > element:
            end = mid - 1
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
