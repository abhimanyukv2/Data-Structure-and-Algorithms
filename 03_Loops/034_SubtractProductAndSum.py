# 1281. Subtract the Product and Sum of Digits of an Integer
# Leetcode

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumOFDigits = 0
        productOFDigits = 1
        while n>0:
            sumOFDigits = sumOFDigits + (n%10)
            productOFDigits = productOFDigits * (n%10)
            n = n//10
        ans = productOFDigits - sumOFDigits
        return ans


# Driver Code
testCase = int(input())
for _ in range(testCase):
    n = int(input())
    obj = Solution()
    ans = obj.subtractProductAndSum(n)
    print(ans)