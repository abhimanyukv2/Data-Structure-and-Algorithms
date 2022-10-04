# 1009. Complement of Base 10 Integer
# 476. Number Complement
# Leetcode


class Solution1:
    def bitwiseComplement(self, n: int) -> int:
        binaryData = format(n,"b")
        # print(binaryData)
        # print(type(binaryData))
        compliment = 0
        ind = 1
        for i in range(-1,-len(binaryData)-1,-1):
            if binaryData[i] == '0':
                compliment = compliment + ind
                ind = ind * 2
            else:
                ind = ind * 2
        return compliment

class solution2:
    def bitwiseComplement(self, n : int) -> int:
        if n == 0:
            return 1
        x = 1
        while x<=n:
            n = n^x
            x = x << 1
        return n

class solution3:
    def bitwiseCompliment(self, n : int) -> int:
        m = n
        mask = 0
        if n == 0:
            return 1
        while m != 0:
            mask = (mask<<1) | 1
            m = m>>1
        ans = (~n) & mask
        return ans

#Driver Code
if __name__ == '__main__':
    testCase = int(input())
    for _ in range(testCase):
        n = int(input())

        obj1 = Solution1()
        ans1 = obj1.bitwiseComplement(n)
        print(ans1)

        obj2 = solution2()
        ans2 = obj2.bitwiseComplement(n)
        print(ans2)

        obj3 = solution3()
        ans3 = obj3.bitwiseCompliment(n)
        print(ans3)