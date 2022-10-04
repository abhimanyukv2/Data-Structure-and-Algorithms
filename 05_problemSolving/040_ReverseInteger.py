# 7. Reverse Integer
# Leetcode

class Solution1:
    def reverse(self, x: int) -> int:
        
        if x>= 2**31-1 or x<= -2**31: 
            return 0
        
        else:
            string = str(x)
            
            if x>=0:
                reverseString = string[::-1]
                
            else:
                temp = string[1:]
                temp2 = temp[::-1]
                reverseString = "-" + temp2
            
            if int(reverseString) >= 2**31-1 or int(reverseString) <= -2**31:
                return 0
            else:
                return int(reverseString)


class solution2:
    def reverse(self, x : int) -> int:
        if x < 0:
            number = -x
        else:
            number = x
        reverseNumber = 0
        while number!=0:
            lastDigit = number%10
            if (reverseNumber > 2**31 - 1)  or (reverseNumber < -2**31):
                return 0
            reverseNumber = reverseNumber*10 + lastDigit
            number = number//10
        if x<0:
            return -reverseNumber
        return reverseNumber

# Driver Code
if __name__ == '__main__':
    testCase = int(input())
    for  _ in range(testCase):
        x = int(input())

        obj1 = Solution1()
        ans1 = obj1.reverse(x)
        print(ans1)

        obj2 = solution2()
        ans2 = obj2.reverse(x)
        print(ans2)