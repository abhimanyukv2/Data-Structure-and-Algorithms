# pass by value

def passByValue(number):
    number = number * 2
    print(number)

number = int(input())
passByValue(number)
print(number)