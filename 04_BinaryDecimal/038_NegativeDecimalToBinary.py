# Negative decimal to binary

class solution1:
    def basicLogic(self, negativeNumber : int) -> int:
        binaryNumber = 0
        i = 0
        if negativeNumber < 0:
            negativeNumber = (2**32) + negativeNumber
        # print(negativeNumber)
        while negativeNumber:
            lastBit = negativeNumber&1
            binaryNumber = ((10**i) * lastBit) + binaryNumber
            negativeNumber = negativeNumber >> 1
            i = i + 1
        return binaryNumber

class solution2:
    def usingBin(self, negativeNumber : int) -> int:
        return bin(negativeNumber)

class solution3:
     def withoutInBuiltFunction(self, negativeNumber : int) -> int:
        return "{0:b}".format(int(negativeNumber))

# Driber code
if __name__ =='__main__':
    testCase = int(input())
    for _ in range(testCase):
        negativeNumber = int(input())

        obj1 = solution1()
        ans1 = obj1.basicLogic(negativeNumber)
        print(ans1)

        obj2 = solution2()
        ans2 = obj2.usingBin(negativeNumber)
        print(ans2)

        obj3 = solution3()
        ans3 = obj3.withoutInBuiltFunction(negativeNumber)
        print(ans3)