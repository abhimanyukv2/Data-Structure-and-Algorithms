# calculating a to the power b

# 1. using operators
class solution1:
    def usingOperators(self, number : int , exponent : int) -> int:
        return number**exponent

# 2. Using loops
class solution2:
    def usingLoops(self, number : int , exponent : int) -> int:
        powerNumber = 1
        for i in range(exponent):
            powerNumber = powerNumber * number
        return powerNumber

# 3. Using function
class solution3:
    def powFunction(self, number : int , exponent : int) -> int:
        return pow(number,exponent)


# Driver code
if __name__ =='__main__':
    testCase = int(input())
    for _ in range(testCase):
        number = int(input())
        exponent = int(input())

        obj1 = solution1()
        ans1 = obj1.usingOperators(number,exponent)
        print(ans1)

        obj2 = solution2()
        ans2 = obj2.usingLoops(number,exponent)
        print(ans2)

        obj3 = solution3()
        ans3 = obj3.powFunction(number,exponent)
        print(ans3)