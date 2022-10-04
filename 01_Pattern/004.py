# print - 16 15 14 13
#         12 11 10 9 
#         8  7  6  5
#         4  3  2  1

n = int(input())
a = n*n
for i in range(n):
    for j in range(n):
        print(a,end=' ')
        a = a - 1
    print()