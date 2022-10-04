# print Prime number

n = int(input())
z = True
for i in range(2,n):
    if n%i == 0:
        print(n,'is not a prime number')
        z = False
        break
    else:
        continue
        
if z == True:
    print(n,'is a Prime Number')
