# Finding SquareRoot of a number

# 1. By improting math library
from math import sqrt
class solution1:
    def usingLibraryFunction(self, number : int) -> int:
        return sqrt(number)

# 2. By using exponention
class solution2:
    def sqrtExponention(self, number : int) -> int:
        return number ** (1/2)


# 3. By using mathematical solution
class solution3:
    def mathmetical(self, number : int) -> int:
        precision = int(input())
        start = 0
        end = number

        while start <= end:
            mid = (start+end)//2

            if mid*mid == number:
                squreroot = mid
                break

            if mid*mid <number:
                squreroot = start
                start = mid + 1
            else:
                end = mid - 1

        increment = 0.1
        for i in range(precision):
            while (squreroot*squreroot <= number):
                squreroot = squreroot + increment

            squreroot = squreroot - increment
            increment = increment/10

        return squreroot


# Driver code
if __name__ == '__main__':
    testCase = int(input())
    for _ in range(testCase):
        number = int(input())

        obj1 = solution1()
        ans1 = obj1.usingLibraryFunction(number)
        print(ans1)

        obj2 = solution2()
        ans2 = obj2.sqrtExponention(number)
        print(ans2)

        obj3 = solution3()
        ans3 = obj3.mathmetical(number)
        print(ans3)