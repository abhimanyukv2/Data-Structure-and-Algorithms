'''
    print -     1 2 3 4
                5 6 7 8
                9 10 11 12
                13 14 15 16
    '''


n = int(input())
a = 1
for i in range(n):
    for j in range(n):
        print(a,end=' ')
        a = a + 1
    print()