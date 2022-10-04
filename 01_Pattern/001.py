'''print -  1 2 3 4
            1 2 3 4
            1 2 3 4
            1 2 3 4'''


n = int(input())
for i in range(n):
    for j in range(1,n+1):
        print(j,end=' ')
    print()