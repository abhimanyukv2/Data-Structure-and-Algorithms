# Function 
# power(number1,number2)

def power1(number1,number2):
    ans = 1
    for i in range(1,number2+1):
        ans = ans * number1
    return ans

number1 = int(input())
number2 = int(input())
print("Answer is",power1(number1,number2))



def power2():
    number1 = int(input())
    number2 = int(input())
    ans = 1
    for i in range(1,number2+1):
        ans = ans * number1
    print("Answer is",ans)

power2()