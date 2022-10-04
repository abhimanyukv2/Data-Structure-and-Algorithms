# Printing Nth fibonacci term
# fibonacci number - 0 1 1 2 3 5 8 13 21 34 55 89 144 ....

def fibonacci(number):
    firsterm = 0
    secondTerm = 1
    for i in range(2,number+1):
        nth_term = firsterm + secondTerm
        firsterm = secondTerm
        secondTerm = nth_term
    return nth_term

nth_term = int(input())
if nth_term == 1:
    print(0)
elif nth_term == 2:
    print(1)
else:
    print(fibonacci(nth_term))