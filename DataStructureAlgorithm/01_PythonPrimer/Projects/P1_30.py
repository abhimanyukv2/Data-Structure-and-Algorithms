'''Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.'''

def repeatedlyDivide1(num):
    if num < 2:
        return 'Please enter greater than 2'
    else:
        ans = 0
        while num >= 2:
            num = num/2
            ans += 1
    return ans

num = int(input())
ans1 = repeatedlyDivide1(num)
print(ans1)