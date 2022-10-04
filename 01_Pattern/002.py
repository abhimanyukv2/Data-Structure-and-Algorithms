'''print -  4 3 2 1
            4 3 2 1
            4 3 2 1
            4 3 2 1'''

n = int(input())
for i in range(n):
    for j in range(n,0,-1):
        print(j,end=' ')
    print()