'''The p-norm of a vector v = ( v1, v2, . . . , vn) in n-dimensional space is defined as ‖v‖= ((v1)**p + (v2)**p + ···+ (vn)**p)**(1/p) .
For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4, 3) has a Euclidean norm of ((4)**2 + (3)**2)**(1/2) = (16 + 9)**(1/2) = √25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.
'''

def norm(v, p):
    p_norm = 0
    for i in v:
        p_norm += i**p
    p_norm = p_norm**(1/p)
    return p_norm

v = list(map(int, input().split()))
p = int(input())
ans = norm(v, p)
print(ans)