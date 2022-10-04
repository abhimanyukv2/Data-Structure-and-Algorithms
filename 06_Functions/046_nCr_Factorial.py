# nCr Programm

def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
    return fact

def nCr(n,r):
    return (factorial(n))//((factorial(r))*factorial(n-r))

n = int(input())
r = int(input())
print(nCr(n,r))