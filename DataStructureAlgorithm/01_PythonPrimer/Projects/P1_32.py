'''Write a Python program that can simulate a simple calculator, using the console as the exclusive input and output device. That is, each input to the calculator, be it a number, like 12.34 or 1034, or an operator, like + or =, can be done on a separate line. After each such input, you should output to the Python console what would be displayed on your calculator.'''

def Addition(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'
    
def Subtraction(number1, number2):    
    return f'{number1} - {number2} = {number1 - number2}'

def Multiplication(number1, number2):
    return f'{number1} * {number2} = {number1 * number2}'

def Division(number1, number2):
    return f'{number1} / {number2} = {number1 / number2}'

def calculator(operation, number1, number2):
    operations = {
        '+': Addition(number1, number2),
        '-': Subtraction(number1, number2),
        '*': Multiplication(number1, number2),
        '/': Division(number1, number2)
    }
    return operations.get(operation, "Invalid Operation! Please select the valid operation")

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("What do you want to do: ")
ans = calculator(operation, number1, number2)
print(ans)