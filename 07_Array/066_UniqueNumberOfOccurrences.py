# LeetCode - 1207. Unique Number of Occurrences
# Given an array of integers arr, 
# return true if the number of occurrences of 
# each value in the array is unique, or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        # print(set(dic.values()))
        # print(set(arr))
        
        if len(set(dic.values())) != len(set(arr)):
            return False
        return True

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        myDict = Counter(arr)
        print(myDict)
        return len(myDict.values()) == len(set(myDict.values()))

# Driver Code
if __name__ == "__main__":
    testCase = int(input())
    for _ in range(testCase):
        arr = list(map(int,input().split()))
        ob = Solution()
        ans = ob.uniqueOccurrences(arr)
        print(ans)