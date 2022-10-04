# print -     * * * *
#             * * *
#             * *
#             *

n = int(input())
for i in range(n):
    a = n - i
    for j in range(a):
        print('*',end=' ')
    print()