# Counting Program

def printCounting1(number):
    for i in range(number+1):
        print(i)

number = int(input())
print(printCounting1(number))

def printCounting2():
    number = int(input())
    for i in range(1,number+1):
        print(i)
    return
printCounting2()