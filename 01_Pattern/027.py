# print -        1 2 3 4 5 5 4 3 2 1
#                1 2 3 4 * * 4 3 2 1
#                1 2 3 * * * * 3 2 1
#                1 2 * * * * * * 2 1
#                1 * * * * * * * * 1

n = int(input())
for i in range(n):
    for j in range(n-i):
        print(j+1,end=' ')
    for j in range(i*2):
        print('*',end=' ')
    for j in range(n-i):
        print(n-j-i,end=' ')
    print()