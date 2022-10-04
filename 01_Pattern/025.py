# print -         1
#               2 3
#             4 5 6
#           7 8 9 10


n = int(input())
a = 1
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print(a,end=' ')
        a = a + 1
    print()