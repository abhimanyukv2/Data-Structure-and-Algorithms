# print Fibonacci number - 0 1 1 2 3 5 8 13 21 34 55 ......



n = int(input())
firstNumber = 0
secondNumber = 1

print(firstNumber,end=' ')
print(secondNumber,end=' ')

for i in range(n):
    nextNumber = firstNumber + secondNumber
    print(nextNumber,end=' ')
    firstNumber = secondNumber
    secondNumber = nextNumber
