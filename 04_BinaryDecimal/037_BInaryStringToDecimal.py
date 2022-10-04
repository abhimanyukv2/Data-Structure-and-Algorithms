# binary string to decimal

# 1. By using inbuilt functions
class solution1:
    def inBuiltFinction(self, binaryNumber : str) -> str:

        # self.binaryNumber = binaryNumber
        decimalNumber = int(binaryNumber,2)
        return decimalNumber


# 2. Without using inbuilt function
class solution2:
    def withoutInBuiltFuntion(self, binaryNumber : str) -> str:
        decimalNumber = 0
        ind = 1
        for i in range(-1,-len(binaryNumber)-1,-1):
            if binaryNumber[i] == '1':
                decimalNumber = decimalNumber + ind
                ind = ind * 2
            else:
                ind = ind * 2
        return decimalNumber

# 3. Binary integer to decimal
class solution3:
    def integerBinaryNumber(self, binaryNumber : int) -> int:
        decimalNumber = 0
        ind = 1
        while binaryNumber > 0:
            if binaryNumber%10 == 1:
                decimalNumber = decimalNumber + ind
                ind = ind * 2
                binaryNumber = binaryNumber//10
            else:
                ind = ind * 2 
                binaryNumber = binaryNumber//10
        return decimalNumber



#Driver code
if  __name__ == '__main__':
    testCase = int(input())
    for _ in range(testCase):
        stringBinaryNumber = input()
        integerBinaryNumber = int(stringBinaryNumber)
        obj = solution1()
        ans = obj.inBuiltFinction(stringBinaryNumber)
        print(ans)
        obj1 = solution2()
        ans1 = obj1.withoutInBuiltFuntion(stringBinaryNumber)
        print(ans1)
        obj2 = solution3()
        ans2 = obj2.integerBinaryNumber(integerBinaryNumber)
        print(ans)
    