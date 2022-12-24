# P-1.29 Write a Python program that outputs all possible strings formed by using the characters 'c' , 'a' , 't' , 'd' , 'o' , and 'g' exactly once.

from itertools import permutations

def permutation1(str):
    return [''.join(x) for x in permutations(str)]

def permutation2(str, i=0):
    ans = []
    if i == len(str):
        ans.append(str)    
    else:
        for j in range(i, len(str)):
            # words = [c for c in strstr
            str[i],str[j] = str[j],str[i]
            permutation2(str, i+1)
            str[i],str[j] = str[j],str[i]

    return ans

str = input()
ans1 = permutation1(str)
print(ans1)

ans2 = permutation2(list(str))
print(ans2)