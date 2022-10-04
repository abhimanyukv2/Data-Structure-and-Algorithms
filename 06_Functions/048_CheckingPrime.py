# Checking prime or not

def isPrime1(number):
    for i in range(2,number):
        if number%i == 0:
            return False
            break
    return True

number = int(input())
if isPrime1(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

