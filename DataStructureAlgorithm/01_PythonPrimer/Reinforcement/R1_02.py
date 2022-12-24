'''Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators'''

def even(k):
    if k&1 == 0:
        return True
    else:
        return False

def is_even(k):
    if (-1)**k == 1:
        return True
    return False

k = int(input())

ans1 = even(k)
print(ans1)

ans2 = is_even(k)
print(ans2)