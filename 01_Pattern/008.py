# print -     1
#             2 3
#             3 4 5
#             4 5 6 7

n = int(input())
for i in range(n):
    a = i
    for j in range(i+1):
        print(a+1,end=' ')
        a = a + 1
    print()

