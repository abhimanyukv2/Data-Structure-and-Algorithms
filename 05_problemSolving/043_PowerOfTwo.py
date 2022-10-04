# 231. Power of Two
# Leetcode

class solution1:
    def isPowerOfTwo(self, n: int) -> int:
        for i in range(31):
            power = pow(2,i)
            if power == n:
                return True
        return False

class solution2:
    def isPowerOfTwo(self, n: int) -> int:
        temp = 1
        while n != temp and temp < (2**32 -1)//2:
            temp = temp * 2
        return n == temp

class solution3:
    def isPowerOfTwo(self, n: int) -> int:
        if n<=0:
            return False
        return (n&(n-1)) == 0

# Driver Code
if __name__ == '__main__':
    testCase = int(input())
    for _ in range(testCase):
        n = int(input())

        obj1 = solution1()
        ans1 = obj1.isPowerOfTwo(n)
        print(ans1)

        obj2 = solution2()
        ans2 = obj2.isPowerOfTwo(n)
        print(ans2)

        obj3 = solution3()
        ans3 = obj3.isPowerOfTwo(n)
        print(ans3)