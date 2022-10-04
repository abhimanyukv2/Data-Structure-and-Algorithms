# 191. Number of 1 Bits
# Leetcode

# 1st solution - By using built in function
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# 2nd Solution - Using bit manuplation
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1: 
                count = count + 1
            n = n >> 1
        return count

# 3rd Solution - Using for loop 

class Solution:
    def hammingWeight(self, n:int) -> int:
        number_of_1s = 0
        for i in range(32):
            if (n&1):   # number_of_1s = number_of_1s + (n&1)
                number_of_1s = number_of_1s + 1

        return number_of_1s


testCase = int(input())
for _ in range(testCase):
    # binaryString = bin(int,input())
    binaryString = int(input(),2)
    # binaryString = bytearray(input(), "utf8")
    obj = Solution()
    ans = obj.hammingWeight(binaryString)
    print(ans)