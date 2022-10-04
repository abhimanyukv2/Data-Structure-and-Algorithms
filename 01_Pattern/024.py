# print -         1
#               2 2
#             3 3 3
#           4 4 4 4


n = int(input())
a = 1
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(a):      # range -> i + 1
        print(a,end=' ')
    a = a + 1
    print()    