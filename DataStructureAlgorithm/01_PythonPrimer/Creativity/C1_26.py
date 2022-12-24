'''Write a short program that takes as input three integers, a, b, and c, from the console and determines if they can be used in a correct arithmetic formula (in the given order), like “a + b = c,” “a = b −c,” or “a ∗b = c.”'''

def arithmetic():
    a = int(input())
    b = int(input())
    c = int(input())

    if ((a+b) == c) or (a == (b-c)) or ((a*b) == c):
        return True
    return False

print(arithmetic())