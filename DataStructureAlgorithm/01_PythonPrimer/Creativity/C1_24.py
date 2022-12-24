'''Write a short Python function that counts the number of vowels in a given character string.'''

def countVowels(string):
    ans = 0
    string.replace(' ','')
    vowels = ['a','e','i','o','u']
    for i in string:
        if i.lower() in vowels:
            ans += 1
    return ans

string = input()
ans = countVowels(string)
print(ans)