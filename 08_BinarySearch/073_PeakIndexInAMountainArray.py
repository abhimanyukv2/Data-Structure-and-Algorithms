''' LeetCode - 852. Peak Index in a Mountain Array
An array arr a mountain if the following properties hold:
arr.length >= 3 There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that 
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
You must solve it in O(log(arr.length)) time complexity.'''

class Solution1:
    def peakIndexInMountainArray(self, arr: list[int]):
        '''This is Linear Search approach
        Time complexity O(n)'''
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return i


class Solution2:
    def peakIndexInMountinArray(self, arr: list[int]) -> int:
        '''This is Binary Search Approach
        Time Comlexity is O(log n)'''
        start = 0
        end = len(arr)-1  # it create TC: O(n)
        while start<end:
            mid = start + (end - start)//2
            if arr[mid]<arr[mid+1]:
                start = mid + 1
            else:
                end = mid

        return start

if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        arr = list(map(int,input().split()))

        ob1 = Solution1()
        ans1 = ob1.peakIndexInMountainArray(arr)
        print(ans1)

        ob2 = Solution2()
        ans2 = ob2.peakIndexInMountinArray(arr)
        print(ans2)