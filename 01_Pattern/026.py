# print -             1
#                   1 2 1
#                 1 2 3 2 1
#               1 2 3 4 3 2 1

n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print(j+1,end=' ')
    for j in range(i):
        print(i-j-1,end=' ')
    print()