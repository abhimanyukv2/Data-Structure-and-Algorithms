'''LeetCode - 724. Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers 
strictly to the left of the index is equal to the 
sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 
because there are no elements to the left. 
This also applies to the right edge of the array. Return the leftmost pivot index. 
If no such index exists, return -1.'''

class Solution1:
    def pivotIndex(self, nums: list[int]) -> int:
        leftsum = 0
        rightsum = sum(nums)
        index = -1
        # Time Complexity = O(n)
        for i in range(len(nums)):
            if leftsum == rightsum- leftsum - nums[i]:
                index = i
                break
            leftsum = leftsum + nums[i]
        return index


if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        nums = list(map(int,input().split()))

        ob1 = Solution1()
        ans = ob1.pivotIndex(nums)
        print(ans)