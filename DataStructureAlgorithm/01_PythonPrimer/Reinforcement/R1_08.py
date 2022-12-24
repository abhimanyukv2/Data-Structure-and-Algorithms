'''Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for index 
−n ≤k < 0, what is the equivalent index j ≥0 such that s[j] references the same element?'''

'''The equivalent index of j is n+k

example: s = 'abcdefghj' n = 10
positive index of element a = 0 = j
negative index of element a = -10 = k

j = n + k = 10 + (-10) = 0

'''

def positiveIndex(negativeIndex, string):
    return len(string) + negativeIndex

string = input()
negativeIndex = int(input())
ans = positiveIndex(negativeIndex, string)
print(ans)