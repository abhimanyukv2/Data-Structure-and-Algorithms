# print -     1
#             2 3
#             3 4 5
#             4 5 6 7

n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end=' ')
        i = i + 1
    print()