# print setbits of two numbers

def setBits(number):
    numberofBits = 0
    while number != 0:
        if number&1:
            numberofBits += 1
        number = number >> 1
    return numberofBits

def totalSetBits(number1,number2):
    return setBits(number1) + setBits(number2)

number1 = int(input())
number2 = int(input())
print(totalSetBits(number1,number2))