# print -     1
#             2 1
#             3 2 1 
#             4 3 2 1

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(i+1,end=' ')
        i = i - 1
    print()