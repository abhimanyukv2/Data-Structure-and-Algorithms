# decimal to Binary

# 1. By using in-Built Function
class solution1:
    def inBuiltFunction(self, decimalNumber : int) -> int:
        return bin(decimalNumber).replace("0b","")


# 2. With out in-Built function
class solution2:
     def withoutInBuiltFunction(self, decimalNumber : int) -> int:
        return "{0:b}".format(int(decimalNumber))

# 3. Quick Ninja Method
class solution3:
    def quickNinjaMethod(self, decimalNumber : int) -> int:
        return bin(decimalNumber)[2:]

# 4. Classic Method
class solution4:
    def classicMethod(self, decimalNumber : int) -> str:
        binaryNumber = ""
        while decimalNumber > 0:
            if decimalNumber%2 == 0:
                binaryNumber = binaryNumber + '0'
                decimalNumber = decimalNumber//2
            else:
                binaryNumber = binaryNumber + '1'
                decimalNumber = decimalNumber//2
        return binaryNumber[::-1]

# Bitwise method
class solution5:
    def bitWiseMethod(self, decimalNumber : int) -> int:
        binaryNumber = 0
        i = 0
        while decimalNumber != 0:
            bit = decimalNumber&1
            binaryNumber = (bit*(10**i)) + binaryNumber
            decimalNumber = decimalNumber >> 1
            i = i + 1
        return binaryNumber


# Driver Code
if __name__ == '__main__':
    testCase = int(input())
    for _ in range(testCase):
        decimalNumber = int(input())

        obj1 = solution1()
        ans1 = obj1.inBuiltFunction(decimalNumber)
        print(ans1)

        obj2 = solution2()
        ans2 = obj2.withoutInBuiltFunction(decimalNumber)
        print(ans2)

        obj3 = solution3()
        ans3 = obj3.quickNinjaMethod(decimalNumber)
        print(ans3)

        obj4 = solution4()
        ans4 = obj4.classicMethod(decimalNumber)
        print(ans4)

        obj5 = solution5()
        ans5 = obj5.bitWiseMethod(decimalNumber)
        print(ans5)