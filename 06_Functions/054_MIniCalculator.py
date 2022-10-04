def miniCalculator(operation):
    switch = {
        '+': number1 + number2,
        '-': number1 - number2,
        '*': number1 * number2,
        '/': number1 / number2
    }
    return switch.get(operation,"Invalid operation! Please select the valid operation")

if __name__ == '__main__':
    number1 = int(input("Enter the First number: "))
    number2 = int(input("Enter the second number: "))
    operation = input()
    print(miniCalculator(operation))