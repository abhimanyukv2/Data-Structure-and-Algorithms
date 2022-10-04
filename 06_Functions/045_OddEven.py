# Even Odd Program

def isEven1(number):
    if number%2 == 0:
        return 1
    return 0

number = int(input())
# isEven1(number)
if isEven1(number):
    print(number,"is Even Number")
else:
    print(number,"is Odd number")



def isEven():
    number = int(input())
    if number&1:
        return "Number is Odd"
    return "Number is Even"
print(isEven())