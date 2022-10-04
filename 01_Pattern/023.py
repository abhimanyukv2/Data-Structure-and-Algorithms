# print -     1 1 1 1
#               2 2 2
#                 3 3
#                   4

n = int(input())
a = 1
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print(a,end=' ')
    a = a + 1
    print()